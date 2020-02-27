# https://leetcode.com/problems/find-median-from-data-stream/
# 295. Find Median from Data Stream
# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
# For example,
# [2,3,4], the median is 3
# [2,3], the median is (2 + 3) / 2 = 2.5
# Design a data structure that supports the following two operations:
#     void addNum(int num) - Add a integer number from the data stream to the data structure.
#     double findMedian() - Return the median of all elements so far.
# Example:
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2
# Follow up:
#     If all integer numbers from the stream are between 0 and 100, how would you optimize it?
#     If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

# Binary Search Solution
class MedianFinder:
    def __init__(self):
        self.data = []
        self.length = 0

    def addNum(self, num):
        l = 0
        r = self.length - 1
        while l <= r:
            m = (l + r)//2
            if self.data[m] >= num:
                r = m - 1
            else:
                l = m + 1
        self.data.insert(l, num)
        self.length += 1

    def findMedian(self):
        if self.length % 2 == 0:
            m = self.length // 2
            return (self.data[m] + self.data[m-1]) / 2
        else:
            return self.data[self.length // 2]
