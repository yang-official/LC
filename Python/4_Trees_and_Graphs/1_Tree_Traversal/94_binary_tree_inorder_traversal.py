# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Given a binary tree, return the inorder traversal of its nodes' values.
# Example:
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Trival Recursive
def inorderTraversal(root):
    result = []
    def _inorder(node):
        if not node:
            return
        _inorder(node.left)
        result.append(node.val)
        _inorder(node.right)
    _inorder(root)
    return result

# Iterative
def inorderTraversal(root):
    result = []
    stack = [(root, "i")]
    while stack:
        node, label = stack.pop()
        if node and label != "c":
            stack.append((node.right, "r"))
            stack.append((node, "c"))
            stack.append((node.left, "l"))
        elif node and label == "c":
            result.append(node.val)
    return result

# Iterative
def inorderTraversal(root):
    result = []
    stack = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            result.append(root.val)
            root = root.right
    return result
