# https://leetcode.com/problems/partition-equal-subset-sum/
# 416. Partition Equal Subset Sum
# Given a non-empty array containing only positive integers, find if the array
# can be partitioned into two subsets such that the sum of elements in both subsets is equal.
# Note:
#     Each of the array element will not exceed 100.
#     The array size will not exceed 200.
# Example 1:
# Input: [1, 5, 11, 5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:
# Input: [1, 2, 3, 5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

# recursive
def canPartition(nums):
	s, n, memo = sum(nums), len(nums), {0: True}
    if s & 1: return False
    nums.sort(reverse=True)
    def dfs(i, x):
        if x not in memo:
            memo[x] = False
            if x > 0:
                for j in range(i, n):
                    if dfs(j+1, x-nums[j]):
                        memo[x] = True
                        break
        return memo[x]
    return dfs(0, s >> 1)
