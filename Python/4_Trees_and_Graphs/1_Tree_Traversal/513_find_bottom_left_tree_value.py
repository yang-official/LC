# https://leetcode.com/problems/find-bottom-left-tree-value/
# 513. Find Bottom Left Tree Value
# Given a binary tree, find the leftmost value in the last row of the tree.
# Example 1:
# Input:
#     2
#    / \
#   1   3
# Output:
# 1
# Example 2:
# Input:
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7
# Output:
# 7
# Note: You may assume the tree (i.e., the given root node) is not NULL.

# Iterative DFS Stack
def findBottomLeftValue(self, root: TreeNode) -> int:
    if not root:
        return
    d = {}
    stack = [(root, 0, 0)]
    while stack:
        node, x, y = stack.pop()
        if y not in d:
            d[y] = {}
        if x not in d[y]:
            d[y][x] = []
        d[y][x].append(node.val)
        if node.left:
            stack.append((node.left, x - 1, y + 1))
        if node.right:
            stack.append((node.right, x + 1, y + 1))
    maxy = max(d.keys())
    minx = min(d[maxy].keys())
    return d[maxy][minx][0]

# Iterative BFS queue
def findBottomLeftValue(self, root: TreeNode) -> int:
    if not root:
        return
    leftmost = None
    queue = [root]
    while queue:
        leftmost = None
        for _ in range(len(queue)):
            node = queue.pop(0)
            if not leftmost:
                leftmost = node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return leftmost.val
