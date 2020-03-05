# https://leetcode.com/problems/valid-palindrome-ii/
# 680. Valid Palindrome II
# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
#     The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

def validPalindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-1-i]:
            t = s[:i] + s[i+1:]
            u = s[:-1-i] + s[len(s)-i:]
            return t==t[::-1] or u == u[::-1]
    return True
