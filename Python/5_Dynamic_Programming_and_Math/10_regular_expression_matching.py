# https://leetcode.com/problems/regular-expression-matching/
# 10. Regular Expression Matching
# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
# Note:
#     s could be empty and contains only lowercase letters a-z.
#     p could be empty and contains only lowercase letters a-z, and characters like . or *.
# Example 1:
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
# Example 5:
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false

def isMatch(s, p):
    dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s)+1)]
    dp[0][0] = True
    for j in range(len(p)):
        if p[j] == '*':
            dp[0][j+1] = dp[0][j-1]
    for i in range(len(s)):
        for j in range(len(p)):
            if p[j] == '*':
                if dp[i+1][j-1]:
                    dp[i+1][j+1] = True
                elif dp[i][j+1] and (p[j-1] == '.' or s[i] == p[j-1]):
                    dp[i+1][j+1] = True
            else:
                if dp[i][j] == True and (s[i] == p[j] or p[j] == '.'):
                    dp[i+1][j+1] = True
    return dp[len(s)][len(p)]
