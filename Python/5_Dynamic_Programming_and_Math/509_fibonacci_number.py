# https://leetcode.com/problems/fibonacci-number/
# 509. Fibonacci Number
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
# Given N, calculate F(N).
# Example 1:
# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:
# Input: 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:
# Input: 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
# Note:
# 0 ≤ N ≤ 30.

# Iterative
def fib(N):
    if N <= 1:
        return N
    a, b = 0, 1
    for _ in range(1, N):
        a, b = b, a + b
    return b

# Recursive with memo
def fib(N):
    memo = {0: 0, 1: 1}
    def _fib(N):
        if N in memo:
            return memo[N]
        return _fib(N-1) + _fib(N-2)
    return _fib(N)
