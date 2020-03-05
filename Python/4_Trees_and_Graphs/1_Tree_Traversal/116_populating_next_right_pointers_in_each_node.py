# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.
# Follow up:
#     You may only use constant extra space.
#     Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
# Example 1:
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
# Constraints:
#     The number of nodes in the given tree is less than 4096.
#     -1000 <= node.val <= 1000

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Iterative BFS
def connect(root):
    if not root:
        return root
    queue = [(root, 0)]
    levels = {}
    while queue:
        node, lvl = queue.pop(0)
        if lvl not in levels:
            levels[lvl] = [node]
        else:
            levels[lvl].append(node)
        if node.left:
            queue.append((node.left, lvl + 1))
        if node.right:
            queue.append((node.right, lvl + 1))
    for l in levels:
        for i in range(len(levels[l])):
            if i + 1 == len(levels[l]):
                levels[l][i].next = None
            else:
                levels[l][i].next = levels[l][i+1]
    return root

# Iterative BFS, no extra space
def connect(root):
    if not root:
        return root
    root.next = None
    queue = [root]
    temp = []
    while queue:
        for i, node in enumerate(queue):
            if i > 0:
                queue[i-1].next = node
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        queue = temp
        temp = []
    return root

# Iterative refactored
def connect(root):
    node = root
    while node and node.left:
        next_lvl = node.left
        while node:
            node.left.next = node.right
            if node.next and node.next.left:
                node.right.next = node.next.left
            else:
                node.right.next = None
            node = node.next
        node = next_lvl
    return root
