# https://leetcode.com/problems/coin-change/
# 322. Coin Change
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
# Example 1:
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.

# Iterative
def coinChange(coins, amount):
    ways = [float('inf')] * (amount + 1)
    ways[0] = 0
    for c in coins:
        for a in range(len(ways)):
            if c <= a:
                ways[a] = min(ways[a-c]+1, ways[a])
    if ways[amount] == float('inf'):
        return -1
    return ways[amount]

# Top down
def coinChange(coins, amount):
    visited = set()
    queue = [amount]
    depth = 0
    while queue:
        size = len(queue)
        while size > 0:
            size -= 1
            left = queue.pop(0)
            if left == 0:
                return depth
            elif left > 0 and left not in visited:
                visited.add(left)
                for c in coins:
                    queue.append(left - c)
        depth += 1
    return -1
