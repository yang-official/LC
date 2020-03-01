# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# 124. Binary Tree Maximum Path Sum
# Given a non-empty binary tree, find the maximum path sum.
# For this problem, a path is defined as any sequence of nodes from some starting
# node to any node in the tree along the parent-child connections. The path must
# contain at least one node and does not need to go through the root.
# Example 1:
# Input: [1,2,3]
#        1
#       / \
#      2   3
# Output: 6
# Example 2:
# Input: [-10,9,20,null,null,15,7]
#    -10
#    / \
#   9  20
#     /  \
#    15   7
# Output: 42

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive
def maxPathSum(root):
    def _maxPath(node):
        if node is None:
            return (float('-inf'), float('-inf'))
        left, lpath = _maxPath(node.left)
        right, rpath = _maxPath(node.right)
        maxSingle = max(left + node.val, right + node.val, node.val)
        maxPath = max(lpath, rpath, maxSingle, node.val + left + right)
        return maxSingle, maxPath
    _, result = _maxPath(root)
    return result
