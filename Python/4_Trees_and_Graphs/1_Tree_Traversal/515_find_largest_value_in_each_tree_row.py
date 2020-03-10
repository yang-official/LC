# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
# 515. Find Largest Value in Each Tree Row
# You need to find the largest value in each row of a binary tree.
# Example:
# Input:
#           1
#          / \
#         3   2
#        / \   \
#       5   3   9
# Output: [1, 3, 9]

# DFS Stack
def largestValues(self, root: TreeNode) -> List[int]:
    if not root:
        return
    d = {}
    stack = [(root, 0)]
    while stack:
        node, lvl = stack.pop()
        if lvl not in d:
            d[lvl] = float('-inf')
        d[lvl] = max(d[lvl], node.val)
        if node.left:
            stack.append((node.left, lvl + 1))
        if node.right:
            stack.append((node.right, lvl + 1))
    return [n for n in d.values()]
