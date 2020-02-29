# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# 442. Find All Duplicates in an Array
# # Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array),
# some elements appear twice and others appear once.
# Find all the elements that appear twice in this array.
# Could you do it without extra space and in O(n) runtime?
# Example:
# Input:
# [4,3,2,7,8,2,3,1]
# Output:
# [2,3]

# Dictionary method, O(N) time, O(N) space
def findDuplicates(nums):
    d = {}
    for n in nums:
        if n not in d:
            d[n] = 0
        d[n] += 1
    result = []
    for k in d:
        if d[k] == 2:
            result.append(k)
    return result

# index tracking, O(N) time, O(1) space
def findDuplicates(nums):
    result = []
    for n in nums:
        n = abs(n)
        if nums[n - 1] < 0:
            result.append(n)
        else:
            nums[n - 1] = - nums[n - 1]
    return result
