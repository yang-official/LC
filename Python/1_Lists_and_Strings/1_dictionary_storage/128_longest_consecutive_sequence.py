# https://leetcode.com/problems/longest-consecutive-sequence/
# 128. Longest Consecutive Sequence
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# Your algorithm should run in O(n) complexity.
# Example:
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# O(n)
def longestConseuctive(nums):
    if not nums:
        return 0
    result = 1
    lengths = {key: 0 for key in nums}
    for i in nums:
        if lengths[i] == 0:
            lengths[i] = 1
            l = lengths.get(i-1, 0)
            r = lengths.get(i+1, 0)
            length = 1 + l + r
            lengths[i - l] = length
            lengths[i + r] = length
            result = max(result, length)
    return result
