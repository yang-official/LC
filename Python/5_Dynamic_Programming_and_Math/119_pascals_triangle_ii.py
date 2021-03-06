# https://leetcode.com/problems/pascals-triangle-ii/
# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
# Note that the row index starts from 0.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
# Example:
# Input: 3
# Output: [1,3,3,1]
# Follow up:
# Could you optimize your algorithm to use only O(k) extra space?

def getRow(rowIndex):
    row = [1]*(rowIndex+1)
    for i in range(1, rowIndex):
        for j in range(i):
            row[i-j] += row[i-j-1]
    return row
