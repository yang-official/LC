# https://leetcode.com/problems/median-of-two-sorted-arrays/
# 4. Median of Two Sorted Arrays
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
# The median is 2.0
# Example 2
# nums1 = [1, 2]
# nums2 = [3, 4]
# The median is (2 + 3)/2 = 2.5

# non-optimal sort O(n log n)
def findMedianSortedArrays(nums1, nums2):
    nums = nums1 + nums2
    nums.sort()
    n = len(nums)
    if n % 2 != 0:
        return nums[n//2]
    else:
        return (nums[n//2] + nums[(n-1)//2]) / 2

# optimal index tracking O(log n)
def findMedianSortedArrays(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError
    imin = 0
    imax = m
    half_len = (m + n + 1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        if i < m and B[j-1] > A[i]:
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            imax = i - 1
        else:
            if i == 0:
                max_of_left = B[j-1]
            elif j == 0:
                max_of_left = A[i-1]
            else:
                max_of_left = max(A[i-1], B[j-1])
            if (m + n) % 2 == 1:
                return max_of_left
            if i == m:
                min_of_right = B[j]
            elif j == n:
                min_of_right = A[i]
            else:
                min_of_right = min(A[i], B[j])
            return (max_of_left + min_of_right) / 2
