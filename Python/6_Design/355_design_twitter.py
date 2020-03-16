# https://leetcode.com/problems/design-twitter/
# Design a simplified version of Twitter where users can post tweets,
# follow/unfollow another user and is able to see the 10 most recent tweets
# in the user's news feed.
# Your design should support the following methods:
#     postTweet(userId, tweetId): Compose a new tweet.
#     getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed.
# Each item in the news feed must be posted by users who the user followed or by the user herself.
# Tweets must be ordered from most recent to least recent.
#     follow(followerId, followeeId): Follower follows a followee.
#     unfollow(followerId, followeeId): Follower unfollows a followee.

from collections import defaultdict
class Twitter:

    def __init__(self): # Initialize data structure
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None: # Compose a new tweet
        self.tweets[userId].insert(0,(self.time,tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Retrieve the 10 most recent tweet ids in the user's news feed.
        # Each item in the news feed must be posted by users who the user
        # followed or by the user herself.
        # Tweets must be ordered from most recent to least recent.
        d = {}
        if userId not in self.follows[userId]:  #user should also see his own posts
            self.follows[userId].add(userId)  #so he should follow himself
        for followee in self.follows[userId]:
            for tweet in self.tweets[followee][0:10]:
                d[tweet[0]] = tweet[1]
        feeds = sorted(d.items(), key=lambda t: t[0], reverse=True) #sort by time
        feed = [i[1] for i in feeds]     # get value from (time,value) pair
        return feed[0:10]                # return only top 10 tweets

    def follow(self, followerId: int, followeeId: int) -> None: # Follower follows a followee
        # If the operation is invalid, it should be a no-op.
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None: # Follower unfollows a followee
        # If the operation is invalid, it should be a no-op
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
