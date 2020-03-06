# https://leetcode.com/problems/binary-tree-level-order-traversal/
# 102. Binary Tree Level Order Traversal
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Iterative BFS
def levelOrder(root):
    if not root:
        return []
    queue = [(root, 0)]
    d = {}
    while queue:
        node, level = queue.pop(0)
        if level not in d:
            d[level] = []
        d[level].append(node.val)
        if node.left:
            queue.append((node.left, level+1))
        if node.right:
            queue.append((node.right, level+1))
    return [d[i] for i in range(len(d))]

# Recursive
def levelOrder(root):
    result = []
    def _traverse(node, level):
        if not node:
            return
        if level == len(result):
            result.append([])
        result[level].append(node.val)
        _traverse(node.left, level + 1)
        _traverse(node.right, level + 1)
    _traverse(root, 0)
    return result
