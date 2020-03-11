# https://leetcode.com/problems/first-missing-positive/
# 41. First Missing Positive
# Given an unsorted integer array, find the smallest missing positive integer.
# Example 1:
# Input: [1,2,0]
# Output: 3
# Example 2:
# Input: [3,4,-1,1]
# Output: 2
# Example 3:
# Input: [7,8,9,11,12]
# Output: 1
# Note:
# Your algorithm should run in O(n) time and uses constant extra space.

def firstMissingPositive(nums):
    i = 1
    while i in nums:
        i += 1
    return i
