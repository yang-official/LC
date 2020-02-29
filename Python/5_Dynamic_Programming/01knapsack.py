# Lacks a direct match leetcode problem
# For problems that are an extension of this problem, see LC 416 and LC 518

# Given a list of items with values and weights, as well as a max weight,
# find the maximum value you can generate from items where the sum of the weights is less than the max.
# eg.
# items = {(w:1, v:6), (w:2, v:10), (w:3, v:12)}
# maxWeight = 5
# knapsack(items, maxWeight) = 22

# Recursive
def knapSack(W, wt, val, n):
    if n == 0 or W == 0 :
        return 0
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), knapSack(W, wt, val, n-1))

# Iterative
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]
