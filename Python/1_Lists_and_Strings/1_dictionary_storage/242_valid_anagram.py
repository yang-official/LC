# https://leetcode.com/problems/valid-anagram/
# 242. Valid Anagram
# Given two strings s and t , write a function to determine if t is an anagram of s.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    d = {}
    for e in s:
        if e not in d:
            d[e] = 0
        d[e] += 1
    for c in t:
        if c not in d:
            return False
        d[c] -= 1
        if d[c] == 0:
            del d[c]
    return len(d) == 0
