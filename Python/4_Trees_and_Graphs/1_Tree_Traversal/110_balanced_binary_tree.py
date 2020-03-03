# https://leetcode.com/problems/balanced-binary-tree/
# 110. Balanced Binary Tree
# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
#     a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
# Example 1:
# Given the following tree [3,9,20,null,null,15,7]:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.
# Example 2:
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive
def isBalanced(root):
    def balance(node):
        if not node:
            return (True, 0)
        left_b, left_h = balance(node.left)
        if not left_b:
            return (False, None)
        right_b, right_h = balance(node.right)
        if not right_b:
            return (False, None)
        if abs(left_h - right_h) > 1:
            return (False, None)
        return (True, max(left_h, right_h) + 1)
    return balance(root)[0]
