# https://leetcode.com/problems/delete-nodes-and-return-forest/
# 1110. Delete Nodes And Return Forest
# Given the root of a binary tree, each node in the tree has a distinct value.
# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
# Return the roots of the trees in the remaining forest.  You may return the result in any order.
# Example 1:
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
# Constraints:
# The number of nodes in the given tree is at most 1000.
# Each node has a distinct value between 1 and 1000.
# to_delete.length <= 1000
# to_delete contains distinct values between 1 and 1000.

def delNodes(root, to_delete):
    forests = []
    to_del = set(to_delete)
    def dfs(node,can_del):
        if node.val in to_del:
            if node.left:
                dfs(node.left,True)
            if node.right:
                dfs(node.right,True)
            return False
        if can_del:
            forests.append(node)
        if node.left and not dfs(node.left,False):
            node.left = None
        if node.right and not dfs(node.right,False):
            node.right = None
        return True
    dfs(root,True)
    return forests
