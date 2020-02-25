# https://leetcode.com/problems/maximum-product-subarray/
# 152. Maximum Product Subarray
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
# Example 1:
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

def maxProduct(nums):
    nprod = [0] * len(nums)
    pprod = [0] * len(nums)
    nprod[0] = nums[0]
    pprod[0] = nums[0]
    for i in range(1, len(nums)):
        pprod[i] = max(nums[i], nums[i]*pprod[i-1], nums[i]*nprod[i-1])
        nprod[i] = min(nums[i], nums[i]*pprod[i-1], nums[i]*nprod[i-1])
    return max(pprod)
