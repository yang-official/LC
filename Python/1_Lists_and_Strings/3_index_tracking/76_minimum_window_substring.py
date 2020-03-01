# https://leetcode.com/problems/minimum-window-substring/
# 76. Minimum Window Substring
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
# Example:
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:
#     If there is no such window in S that covers all characters in T, return the empty string "".
#     If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

def minWindow(s, t):
    if len(s) < len(t):
        return ""
    d = {}
    for c in t:
        if c not in d:
            d[c] = 0
        d[c] += 1
    missing = len(t)
    l = L = R = 0
    for r, c in enumerate(s, 1):
        if c in d and d[c] > 0:
            missing -= 1
        if c in d:
            d[c] -= 1
        while l < r and not missing:
            if not R or r - l < R - L:
                L, R = l, r
            if s[l] not in d:
                l += 1
            else:
                d[s[l]] += 1
                if d[s[l]] > 0:
                    missing += 1
                l += 1
    return s[L:R]
