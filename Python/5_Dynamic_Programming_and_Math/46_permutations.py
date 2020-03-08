# https://leetcode.com/problems/permutations/
# Given a collection of distinct integers, return all possible permutations.
# Example:
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

def permute(nums):
    result = []
    def _permute(arr, aux_arr):
        if not arr:
            result.append(aux_arr)
            return
        for i in range(len(arr)):
            _permute(arr[:i] + arr[i+1:], aux_arr+[arr[i]])
    _permute(nums, [])
    return result

# library imports
from itertools import permutations
def permute(nums: List[int]) -> List[List[int]]:
    return list(permutations(nums))
