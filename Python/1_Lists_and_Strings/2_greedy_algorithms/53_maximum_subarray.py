# https://leetcode.com/problems/maximum-subarray/
# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and return its sum.
# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution
# using the divide and conquer approach, which is more subtle.

# Without finding subarray
def maxSubArray(nums):
    sums = [0] * len(nums)
    sums[0] = nums[0]
    for i in range(1, len(nums)):
        sums[i] = max(nums[i], nums[i] + sums[i-1])
    return max(sums)

# With finding subarray index
def maxSubArray(nums):
    sums = [0] * len(nums)
    sums[0] = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > nums[i] + sums[i-1]:
            sums[i] = nums[i]
            l = i
        else:
            sums[i] = nums[i] + sums[i-1]
    r = sums.index(max(sums))
    return max(sums)
