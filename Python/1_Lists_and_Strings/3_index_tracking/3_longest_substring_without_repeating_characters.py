# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 3. Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.
# Example 1
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(s):
    d = {}
    L = 0
    m = 0
    for R, c in enumerate(s):
        if c not in d or d[c] < L:
            m = max(m, R - L + 1)
            d[c] = R
        else:
            L = d[c] + 1
            d[c] = R
    return m
