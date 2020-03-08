# https://leetcode.com/problems/search-a-2d-matrix/
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#     Integers in each row are sorted from left to right.
#     The first integer of each row is greater than the last integer of the previous row.
# Example 1:
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# Example 2:
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false

# Binary Search O(max(log n, log m))
def searchMatrix(matrix, target):
    if len(matrix) == 0:
        return False
    top, bottom = 0, len(matrix) - 1
    while top < bottom:
        middle = (top + bottom) // 2 + 1
        if matrix[middle][0] == target:
            return True
        elif matrix[middle][0] < target:
            top = middle
        else:
            bottom = middle - 1
    left, right = 0, len(matrix[0]) - 1
    while left <= right:
        middle = (left + right) // 2
        if matrix[top][middle] == target:
            return True
        elif matrix[top][middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return False

# Brute Force O(n*m) time
def searchMatrix(matrix, target):
    x, y = 0, 0
    while x < len(matrix):
        if matrix[x][0] < target:
            x += 1
        elif matrix[x][0] == target:
            return True
        else:
            break
    while y < len(matrix[x]):
        if matrix[x][y] < target:
            x += 1
        elif matrix[x][y] == target:
            return True
        else:
            return False
    return False
