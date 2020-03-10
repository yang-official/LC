# https://leetcode.com/problems/jump-game-iii/
# Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.
# Notice that you can not jump outside of the array at any time.
# Example 1:
# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation:
# All possible ways to reach at index 3 with value 0 are:
# index 5 -> index 4 -> index 1 -> index 3
# index 5 -> index 6 -> index 4 -> index 1 -> index 3
# Example 2:
# Input: arr = [4,2,3,0,3,1,2], start = 0
# Output: true
# Explanation:
# One possible way to reach at index 3 with value 0 is:
# index 0 -> index 4 -> index 1 -> index 3
# Example 3:
# Input: arr = [3,0,2,1,2], start = 2
# Output: false
# Explanation: There is no way to reach at index 1 with value 0.

# BFS with Queue
def canReach(self, arr: List[int], start: int) -> bool:
    N = len(arr)
    seen = set()
    queue = [start]
    while queue:
        i = queue.pop(0)
        if arr[i] == 0:
            return True
        seen.add(i)
        for v in [i - arr[i], i + arr[i]]:
            if v not in seen and -1 < v < N:
                queue.append(v)
    return False

# DFS with Stack
