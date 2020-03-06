# https://leetcode.com/problems/decode-ways/
# 91. Decode Ways
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
# Example 1:
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

def numDecodings(s):
    memo = {}
    def _decode(s):
        if len(s) == 0:
            return 1
        if s in memo:
            return memo[s]
        takeOne = takeTwo = 0
        if int(s[:1]) >= 1 and int(s[:1]) <= 9:
            takeOne = _decode(s[:1])
        if int(s[:2]) >= 10 and int[s:2]) <= 26:
            takeTwo = _decode(s[:2])
        memo[s] = takeOne + takeTwo
        return memo[s]
    return _decode(s)
