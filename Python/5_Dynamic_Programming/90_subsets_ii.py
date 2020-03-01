# https://leetcode.com/problems/subsets-ii/
# 90. Subsets II
# Given a collection of integers that might contain duplicates, nums,
# return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.
# Example:
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

# Iterative
def subsetsWithDup(nums):
    result = [[]]
    for n in sorted(nums):
        for r in result[:len(result)]:
            if r + [n] not in result:
                result.append(r + [n])
    return result
