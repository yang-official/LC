# https://leetcode.com/problems/combination-sum/
# 39. Combination Sum
# Given a set of candidate numbers (candidates) (without duplicates)
# and a target number (target), find all unique combinations in candidates
# where the candidate numbers sums to target.
# The same repeated number may be chosen from candidates unlimited number of times.
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

def cominationSum(candidates, target):
    result = []
    pool = [([], 0)]
    for n in candidates:
        for (ls, v) in pool:
            if v + n == target:
                result.append(ls + [n])
            elif v + n < target:
                pool.append((ls + [n], v + n))
    return result
