# https://leetcode.com/problems/merge-intervals/
# 56. Merge Intervals
# Given a collection of intervals, merge all overlapping intervals.
# Example 1:
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

def merge(intervals):
    result = []
    if not intervals:
        return result
    intervals.sort(key=lambda x: x[0])
    L, R = intervals[0]
    for i in intervals[1:]:
        if i[0] > R:
            result.append([L, R])
            L, R = i
        else:
            R = max(i[1], R)
    result.append([L, R])
    return result