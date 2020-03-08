# https://leetcode.com/problems/maximal-square/
# 221. Maximal Square
# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
# Example:
# Input:
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Output: 4

def maximalSquare(matrix):
    if matrix == []:
        return 0
    dp = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
    maxs = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == "1":
                dp[x+1][y+1] = min(dp[x][y], dp[x][y+1], dp[x+1][y]) + 1
                maxs = max(maxs, dp[x+1][y+1])
    return maxs**2
