# https://leetcode.com/problems/course-schedule-ii/
# 210. Course Schedule II
# There are a total of n courses you have to take, labeled from 0 to n-1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
# Example 1:
# Input: 2, [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
#              course 0. So the correct course order is [0,1] .
# Example 2:
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
#              courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
#              So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
# Note:
#     The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
#     You may assume that there are no duplicate edges in the input prerequisites.

def findOrder(numCourses, prerequisites):
    graph = [[] for i in range(numCourses)]
    indegree = [0 for i in range(numCourses)]
    for pre in prerequisites:
        indegree[pre[0]] += 1
        graph[pre[1]].append(pre[0])
    queue = []
    for i in range(len(indegree)):
        if not indegree[i]:
            queue.append(i)
    count = 0
    result = []
    while queue:
        curr = queue.pop(0)
        result.append(curr)
        count += 1
        for i in range(len(graph[curr])):
            indegree[graph[curr][i]] -= 1
            if indegree[graph[curr][i]] == 0:
                queue.append(graph[curr][i])
    if len(result) != numCourses:
        return []
    return result
