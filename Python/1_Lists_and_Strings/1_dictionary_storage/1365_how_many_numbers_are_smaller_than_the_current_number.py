# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
# 1365. How Many Numbers Are Smaller Than the Current Number
# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.
# Example 1:
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation:
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1).
# For nums[3]=2 there exist one smaller number than it (1).
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
# Example 2:
# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]
# Example 3:
# Input: nums = [7,7,7,7]
# Output: [0,0,0,0]
# Constraints:
#     2 <= nums.length <= 500
#     0 <= nums[i] <= 100

# Brute Force O(N^2)
def smallerNumbersThanCurrent(nums):
    result = [0] * len(nums)
    for i, e in enumerate(nums):
        for j in range(len(nums)):
            if i != j and nums[j] < e:
                result[i] += 1
    return result

# Extra Space buckets O(N)
def smallerNumbersThanCurrent(nums):
    bucket = [0] * 101
    for n in nums:
        bucket[n] += 1
    accum = [0] * 101
    for i in range(1, 101):
        accum[i] = accum[i-1] + bucket[i-1]
    return [accum[n] for n in nums]
