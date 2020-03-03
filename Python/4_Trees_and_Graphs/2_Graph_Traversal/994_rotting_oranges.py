# https://leetcode.com/problems/rotting-oranges/
#994. Rotting Oranges
# In a given grid, each cell can have one of three values:
#     the value 0 representing an empty cell;
#     the value 1 representing a fresh orange;
#     the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
# Example 1:
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
# Note:
#     1 <= grid.length <= 10
#     1 <= grid[0].length <= 10
#     grid[i][j] is only 0, 1, or 2.

# Iterative BFS
def orangesRotting(grid):
    queue = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 2:
                queue.append((x, y, 0))
    t = 0
    while queue:
        x, y, t = queue.pop(0)
        if x < len(grid)-1 and grid[x+1][y] == 1:
            grid[x+1][y] = 2
            queue.append((x+1,y,t+1))
        if y < len(grid[0]) - 1 and grid[x][y+1] == 1:
            grid[x][y+1] = 2
            queue.append((x,y+1,t+1))
        if x > 0 and grid[x-1][y] == 1:
            grid[x-1][y] = 2
            queue.append((x-1,y,t+1))
        if y > 0 and grid[x][y-1] == 1:
            grid[x][y-1] = 2
            queue.append((x,y-1,t+1))
    fresh = [1 in row for row in grid]
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 1:
                return -1
    return t
