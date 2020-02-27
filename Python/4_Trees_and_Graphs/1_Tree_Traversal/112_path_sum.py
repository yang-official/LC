# https://leetcode.com/problems/path-sum/
# 112. Path Sum
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
# Note: A leaf is a node with no children.
# Example:
# Given the below binary tree and sum = 22,
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive
def hasPathSum(root, sum):
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == sum
    return hasPathSum(root.left, sum - root.val) or hasPathSum(root.right, sum - root.val)

# Iterative BFS
def hasPathSum(root, sum):
    if not root:
        return False
    queue = [(root, sum)]
    while queue:
        node, sum = queue.pop()
        if not node.left and not node.right:
            if node.val == sum:
                return True
        if node.left:
            queue.append([node.left, sum - node.val])
        if node.right:
            queue.append([node.right, sum - node.val])
    return False

# Iterative DFS
def hasPathSum(root, sum):
    if not root:
        return False
    stack = [(root, sum)]
    while stack:
        node, sum = stack.pop(0)
        if not node.left and not node.right:
            if node.val == sum:
                return True
        if node.left:
            stack.append([node.left, sum - node.val])
        if node.right:
            stack.append([node.right, sum - node.val])
    return False
