# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
# 1277. Count Square Submatrices with All Ones
# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
# Example 1:
# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation:
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.
# Example 2:
# Input: matrix =
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# Output: 7
# Explanation:
# There are 6 squares of side 1.
# There is 1 square of side 2.
# Total number of squares = 6 + 1 = 7.
# Constraints:
#     1 <= arr.length <= 300
#     1 <= arr[0].length <= 300
#     0 <= arr[i][j] <= 1

# Math
def countSquares(matrix):
    for x in range(1, len(matrix)):
        for y in range(1, len(matrix[0])):
            matrix[x][y] = matrix[x][y] and min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
        return sum([sum(row) for row in matrix])

# Dynamic Programming
# dp[i+1][j+1] == the number of squares ended at matrix[i][j](lower right corner)
def countSquares(matrix):
    dp = [[0 for _ in range(1+len(matrix[0]))] for _ in range(1 + len(matrix))]
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            dp[x+1][y+1] = min(dp[x][y], dp[x][y+1], dp[x+1][y]) + 1 if matrix[x][y] == 1 else 0
    return sum([sum(row) for row in dp])
