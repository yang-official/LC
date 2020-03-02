# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# 1022. Sum of Root To Leaf Binary Numbers
# Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
# Return the sum of these numbers.
# Example 1:
# Input: [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
# Note:
#     The number of nodes in the tree is between 1 and 1000.
#     node.val is 0 or 1.
#     The answer will not exceed 2^31 - 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive
def sumRootToLeaf(root):
    leaves = []
    def _sum(node, num):
        if not node.left and not node.right:
            leaves.append(num)
        if node.left:
            _sum(node.left, num + str(node.val))
        if node.right:
            _sum(node.right, num + str(node.val))
    _sum(root, str(root.val))
    total = 0
    for l in leaves:
        n = len(l)
        for i, d in enumerate(l):
            total += int(d) * 2**(n-i-1)
    return total

# Iterative DFS
def sumRootToLeaf(root):
    if not root:
        return None
    stack = [(root, '')]
    leaves = []
    while stack:
        node, num = stack.pop()
        num += str(node.val)
        if not node.left and not node.right:
            leaves.append(num)
        if node.left:
            stack.append((node.left, num))
        if node.right:
            stack.append((node.right, num))
    total = 0
    for l in leaves:
        n = len(l)
        for i, d in enumerate(l):
            total += int(d) * 2**(n-i-1)
    return total
