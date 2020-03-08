# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Given a binary tree, flatten it to a linked list in-place.
# For example, given the following tree:
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

# Recursive
def flatten(root): # modify root in-place
    def _traverse(node):
        if not node:
            return
        l, r = node.left, node.right
        node.left, node.right = None, l
        _traverse(l)
        while node.right:
            node = node.right
        node.right = r
        _traverse(r)
    _traverse(root)

# Iterative DFS
def flatten(root):
    stack = [root]
    parent = None
    while stack:
        node = stack.pop()
        if node:
            stack += [node.right, node.left]
            if parent:
                parent.left = None
                parent.right = node
            parent = node
