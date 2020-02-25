# https://leetcode.com/problems/longest-palindromic-substring/
# 5. Longest Palindromic Substring
# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.
# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
# Input: "cbbd"
# Output: "bb"

def longestPalindrome(s):
    if len(s) < 2:
        return s
    start = 0
    maxlen = 1
    i = 0
    while i < len(s):
        L, R = i, i
        while R < len(s) - 1 and s[R] == s[R+1]:
            R += 1
        i = R + 1
        while R < len(s) - 1 and L > 0 and s[R+1] == s[L-1]:
            L -= 1
            R += 1
        if maxlen < R - L + 1:
            start = L
            maxlen = R - L + 1
    return s[start:start+maxlen]
