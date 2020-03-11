# https://leetcode.com/problems/largest-rectangle-in-histogram/
# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
# Example:
# Input: [2,1,5,6,2,3]
# Output: 10

def largestRectangleArea(self, heights: List[int]) -> int:
    maxarea = 0
    stack = []
    heights.append(0)
    i = 0
    while i < len(heights):
        if not stack or heights[stack[-1]] <= heights[i]:
            stack.append(i)
            i += 1
        else:
            j = stack.pop()
            h = heights[j]
            w = i
            if stack:
                w = i - stack[-1] - 1
            maxarea = max(maxarea, h * w)
    return maxarea
