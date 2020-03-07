# https://leetcode.com/problems/subarray-sum-equals-k/
# 560. Subarray Sum Equals K
# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
#     The length of the array is in range [1, 20,000].
#     The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

# Dictionary, space O(N) time O(N)
def subarraySum(nums, k):
    count = 0
    csum = 0
    d = {0: 1}
    for n in nums:
        csum += n
        if csum - k in d:
            count += d[csum - k]
        if csum not in d:
            d[csum] = 1
        else:
            d[csum] += 1
    return count

# Brute Force time O(N^2)
def subarraySum(nums, k):
    count = 0
    for i in range(len(nums)-1):
        for j in range(i, len(nums)):
            if sum(nums[i:j]) == k:
                count += 1
    return count

# Variant: find subarray that sums to 0
def zeroSum(nums):
    d = {}
    csum = 0
    for i in range(len(nums)):
        if csum not in d:
            d[csum] = i
            csum += nums[i]
        else:
            return nums[d[csum]:i]
    return None
