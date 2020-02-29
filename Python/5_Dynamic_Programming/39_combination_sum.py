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

# Iterative
def combinationSum(candidates, target):
    result = []
    pool = [ ( [], 0 ) ]
    for n in candidates:
        for intermediate, value in pool:
            if value + n == target:
                result.append(intermediate + [n])
            elif value + n < target:
                pool.append( (intermediate + [n], value + n) )
    return result

# Recursive
def combinationSum(candidates, target):
    def _combination(candidates, target, intermediate, result, i):
        if target == 0:
            result.append(list(intermediate))
        while i < len(candidates) and candidates[i] <= target:
            intermediate.append(candidates[i])
            _combination(candidates, target - candidates[i], intermediate, result, i)
            intermediate.pop()
            i += 1
    result = []
    _combination(sorted(candidates), target, [], result, 0)
    return result

# Recursive refactored
def combinationSum(candidates, target):
    result = []
    def _combination(intermediate, candidates):
        if sum(intermediate) == target:
            result.append(intermediate)
            return True
        elif sum(intermediate) > target:
            return True
        else:
            for i, n in enumerate(candidates):
                if _combination(intermediate + [n], candidates[i:]):
                    break
    _combination([], sorted(candidates))
    return result
