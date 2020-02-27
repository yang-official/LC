# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# 104. Maximum Depth of Binary Tree
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Note: A leaf is a node with no children.
# Example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive
def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

# Iterative DFS
def maxDepth(root):
    if root is None:
        return 0
    mdepth = 0
    stack = [(root, 1)]
    while stack:
        node, level = stack.pop(0)
        mdepth = max(mdepth, level)
        if node.left:
            stack.append([node.left, level+1])
        if node.right:
            stack.append([node.right, level+1])
    return mdepth
