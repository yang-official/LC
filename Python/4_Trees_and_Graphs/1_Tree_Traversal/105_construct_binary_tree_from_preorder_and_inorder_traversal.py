# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Given preorder and inorder traversal of a tree, construct the binary tree.
# Note:
# You may assume that duplicates do not exist in the tree.
# For example, given
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:
#     3
#    / \
#   9  20
#     /  \
#    15   7

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Iterative
def buildTree(preorder, inorder):
    if len(preorder) == 0:
        return None
    head = TreeNode(preorder[0])
    stack = [head]
    i = 1 # preorder index
    j = 0 # inorder index
    while i < len(preorder):
        temp = None
        t = TreeNode(preorder[i])
        while stack and stack[-1].val == inorder[j]:
            temp = stack.pop()
            j += 1
        if temp:
            temp.right = t
        else:
            stack[-1].left = t
        stack.append(t)
        i += 1
    return head

# Recursive
def buildTree(preorder, inorder):
    if len(inorder) == 0:
        return None
    i = inorder.index(preorder[0])
    root = TreeNode(preorder[0])
    root.left = buildTree(preorder[1:], inorder[:i])
    root.right = buildTree(preorder[i+1:], inorder[i+1:])
    return root
