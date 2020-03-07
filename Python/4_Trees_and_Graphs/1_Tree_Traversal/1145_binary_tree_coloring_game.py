# https://leetcode.com/problems/binary-tree-coloring-game/discuss/?currentPage=1&orderBy=hot&query=&tag=python-3
# 1145. Binary Tree Coloring Game
# Two players play a turn based game on a binary tree.  We are given the root of this binary tree, and the number of nodes n in the tree.  n is odd, and each node has a distinct value from 1 to n.
# Initially, the first player names a value x with 1 <= x <= n, and the second player names a value y with 1 <= y <= n and y != x.  The first player colors the node with value x red, and the second player colors the node with value y blue.
# Then, the players take turns starting with the first player.  In each turn, that player chooses a node of their color (red if player 1, blue if player 2) and colors an uncolored neighbor of the chosen node (either the left child, right child, or parent of the chosen node.)
# If (and only if) a player cannot choose such a node in this way, they must pass their turn.  If both players pass their turn, the game ends, and the winner is the player that colored more nodes.
# You are the second player.  If it is possible to choose such a y to ensure you win the game, return true.  If it is not possible, return false.
# Example 1:
# Input: root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
# Output: true
# Explanation: The second player can choose the node with value 2.
# Constraints:
#     root is the root of a binary tree with n nodes and distinct node values from 1 to n.
#     n is odd.
#     1 <= x <= n <= 100

# Recursive
def btreeGameWinningMove(root, n, x):
    def find_x(node, child_count, x):
        if not node:
            return 0
        l = find_x(node.left, child_count, x)
        r = find_x(node.right, child_count, x)
        if node.val == x:
            child_count[0] = l
            child_count[1] = r
            return 0
        return l + r + 1
    counts = [0, 0, 0]
    counts[2] = find_x(root, counts, x)
    return any(counts[i] > n - counts[i] for i in range(3))

# Iterative DFS
def btreeGameWinningMove(root: TreeNode, n: int, x: int) -> bool:
    stack = [(root, 0)]
    count = [0] * 3 # [0] - nodes not descendant of x, [1] descendants of x.left, [2] descendants of x.right
    while stack:
        node, i = stack.pop()
        if node.val != x:
            count[i] += 1
            if node.left:
                stack.append((node.left, i))
            if node.right:
                stack.append((node.right, i))
        else:
            if node.left:
                stack.append((node.left, 1))
            if node.right:
                stack.append((node.right, 2))
    for c in count:
        if c > n - c:
            return True
    return False
