# https://leetcode.com/problems/sort-an-array/
# 912. Sort an Array
# Given an array of integers nums, sort the array in ascending order.
# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Constraints:
#     1 <= nums.length <= 50000
#     -50000 <= nums[i] <= 50000

# Merge Sort, O(n log n)
def sortArray(nums):
    def mergeSort(A, L, R):
        if L < R:
            M = (L + R)//2
            mergeSort(A, L, M), mergeSort(A, M+1, R)
            merge(A, L, M, R)
    def merge(A, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L, R = [0] * n1, [0] * n2
        for i in range(n1):
            L[i] = A[l+i]
        for j in range(n2):
            R[j] = A[m + 1 + j]
        i, j, k = 0, 0, 1
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        while i < n1:
            A[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            A[k] = R[j]
            j += 1
            k += 1
    mergeSort(nums, 0, len(nums))
    return nums

# Quick Sort (in-place): average O(n log n), worst O(n^2)
def sortArray(nums):
    def quicksort(A, L, R):
        if L < R:
            p = partition(A, L, R)
            quickSort(A, L, p-1), quickSort(A, p+1, R)
    def partition(A, l, r):
        i = l - 1
        pivot = A[r]
        for j in range(l, r):
            if A[j] <= pivot:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i+1], A[r] = A[r], A[i+1]
        return i + 1
    quicksort(nums, 0, len(nums))
    return nums

# Quick Sort refactored, uses extra space
def sortArray(nums):
    def quicksort(nums):
        if len(nums) <= 1:
            return nums
        pivot = nums[0] # or random choice
        l = [n for n in nums if n < pivot]
        e = [n for n in nums if n == pivot]
        r = [n for n in nums if n > pivot]
        return quicksort(l) + e + quicksort(r)
    return quicksort(nums)

# Count Sort: O(n+k) where k is max(nums) - min(nums)
def sortArray(nums):
    d = {}
    for n in nums:
        if n not in d:
            d[n] = 0
        d[n] += 1
    mi = min(nums)
    ma = max(nums)
    result = []
    for n in range(mi, ma+1):
        if n in d:
            result += [n] * d[n]
    return result

# Cheat sort
def sortArray(nums):
    return sorted(nums)
