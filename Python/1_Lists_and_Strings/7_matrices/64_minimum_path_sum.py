# https://leetcode.com/problems/minimum-path-sum/
# 64. Minimum Path Sum
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.
# Example:
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

def minPathSum(grid):
    for x in range(1, len(grid)):
        grid[x][0] = grid[x-1][0] + grid[x][0]
    for y in range(1, len(grid[0])):
        grid[0][y] = grid[0][y-1] + grid[0][y]
    for x in range(1, len(grid)):
        for y in range(1, len(grid[0])):
            grid[x][y] = min(grid[x-1][y] + grid[x][y], grid[x][y-1] + grid[x][y])
    return grid[-1][-1]

# Variant, maximum product path
def maxPathProd(grid):
    maxPath = grid.copy()
    minPath = grid.copy()
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if x == 0 and y == 0:
                minval, maxval = grid[0][0]
            if x > 0:
                tempmax = max(grid[x][y] * maxPath[x-1][y], grid[x][y] * minPath[x-1][y])
                tempmin = min(grid[x][y] * maxPath[x-1][y], grid[x][y] * minPath[x-1][y])
                maxval = max(tempmax, maxval)
                minval = min(tempmin, minval)
            if y > 0:
                tempmax = max(grid[x][y] * maxPath[x][y-1], grid[x][y] * minPath[x][y-1])
                tempmin = min(grid[x][y] * maxPath[x][y-1], grid[x][y] * minPath[x][y-1])
                maxval = max(tempmax, maxval)
                minval = min(tempmin, minval)
            maxPath[x][y] = maxval
            minPath[x][y] = minval
    return maxPath[-1][-1]
