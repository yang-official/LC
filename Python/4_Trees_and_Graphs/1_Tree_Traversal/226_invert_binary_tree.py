# https://leetcode.com/problems/invert-binary-tree/
# 226. Invert Binary Tree
# Invert a binary tree.
# Example:
# Input:
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
#     Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive
def invertTree(root):
    if not root:
        return root
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root

# Iterative DFS
def invertTree(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if not node:
            continue
        stack.extend([node.left, node.right])
        node.left, node.right = node.right, node.left
    return root

# Iterative BFS
def invertTree(root):
    queue = [root]
    while queue:
        node = queue.pop(0)
        if not node:
            continue
        queue.extend([node.left, node.right])
        node.left, node.right = node.right, node.left
    return root
