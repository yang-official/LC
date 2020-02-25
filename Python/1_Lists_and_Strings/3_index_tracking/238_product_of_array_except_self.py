# https://leetcode.com/problems/product-of-array-except-self/
# 238. Product of Array Except Self
# Given an array nums of n integers where n > 1,
# return an array output such that output[i] is equal
# to the product of all the elements of nums except nums[i].
# Example:
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Note: Please solve it without division and in O(n).
# Follow up:
# Could you solve it with constant space complexity?
# (The output array does not count as extra space for the purpose of space complexity analysis.)

def getProducts(nums):
    n = len(nums)
    output = [1] * n
    left = 1
    for i in range(n):
        output[i] *= left
        left *= nums[i]
    right = 1
    for i in reversed(range(n)):
        output[i] *= right
        right *= nums[i]
    return output
