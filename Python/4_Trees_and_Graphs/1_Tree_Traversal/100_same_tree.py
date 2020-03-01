# # https://leetcode.com/problems/same-tree/
# 100. Same Tree
# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
# Example 1:
# Input:     1         1
#           / \       / \
#          2   3     2   3
#         [1,2,3],   [1,2,3]
# Output: true
# Example 2:
# Input:     1         1
#           /           \
#          2             2
#         [1,2],     [1,null,2]
# Output: false
# Example 3:
# Input:     1         1
#           / \       / \
#          2   1     1   2
#         [1,2,1],   [1,1,2]
# Output: false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive
def isSameTree(p, q):
    if not p and not q:
        return True
    if (not p or not q) or (p.val != q.val):
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# Iterative DFS
def isSameTree(p, q):
    stack = [(p, q)]
    while stack:
        p, q = stack.pop()
        if not p and not q:
            continue
        if (not p or not q) or (p.val != q.val):
            return False
        stack.extend([(q.right, p.right), (q.left, p.left)])
    return True

# Iterative BFS
def isSameTree(p, q):
    queue = [(p, q)]
    while queue:
        p, q = queue.pop(0)
        if not p and not q:
            continue
        elif (not p or not q) or (p.val != q.val):
            return False
        queue.extend([(p.left, q.left), (p.right, q.right)])
    return True
