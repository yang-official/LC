# https://leetcode.com/problems/subsets/
# 78. Subsets
# Given a set of distinct integers, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.
# Example:
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

# Recursive
def subsets(nums):
    if not nums:
        return [[]]
    prefix = subsets(nums[:-1])
    return prefix + [pre + nums[-1] for pre in prefix]

# Iterative
def subsets(nums):
    result = [[]]
    for n in nums:
        result += [r + [num] for r in result]
    return result
