# https://leetcode.com/problems/interleaving-string/
# 97. Interleaving String
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
# Example 1:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Example 2:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        l = len(s3)
        if l != m+n:
            return False
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(0,m+1):
            dp[i][0]  = (s1[:i] == s3[:i])
        for j in range(0,n+1):
            dp[0][j] = (s2[:j] == s3[:j])

        for i in range(1,m+1):
            count = i
            for j in range(1,n+1):
                dp[i][j] = (dp[i-1][j] and (s3[count] == s1[i-1])) or (dp[i][j-1] and (s3[count] == s2[j-1]))
                count += 1
        return dp[m][n]
