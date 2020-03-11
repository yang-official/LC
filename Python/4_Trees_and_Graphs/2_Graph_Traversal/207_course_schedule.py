# https://leetcode.com/problems/course-schedule/
# 207. Course Schedule
# There are a total of n courses you have to take, labeled from 0 to n-1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
# Example 1:
# Input: 2, [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
# Note:
#     The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
#     You may assume that there are no duplicate edges in the input prerequisites.

def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = [[] for _ in range(numCourses)]
    degree = [0 for _ in range(numCourses)]
    for c in prerequisites:
        degree[c[0]] += 1
        graph[c[1]].append(c[0])
    queue = []
    for i in range(len(degree)):
        if not degree[i]:
            queue.append(i)
    count = 0
    while queue:
        cur = queue.pop(0)
        count += 1
        for i in range(len(graph[cur])):
            degree[graph[cur][i]] -= 1
            if degree[graph[cur][i]] == 0:
                queue.append(graph[cur][i])
    return numCourses == count
# Initially we add all the courses withought any prerequisite to our queue.
# As long as this queue is not empty we pick a course and update the dictionaries.
# SO if we pick 2 we find [3,4] using pre dictionary and for each we decrement their
# value by one in the count dictionary. If the count dictionary for any of them
# is zero it means that their prerequisites have been met and they are ready to be
# picked so we add them to the queue.
