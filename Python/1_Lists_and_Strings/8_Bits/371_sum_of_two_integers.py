# https://leetcode.com/problems/sum-of-two-integers/
# 371. Sum of Two Integers
# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
# Example 1:
# Input: a = 1, b = 2
# Output: 3
# Example 2:
# Input: a = -2, b = 3
# Output: 1

# Bits
def getSum(a, b):
    while b & 0xffffffff: # b & 0xffffffff will remain the same as b
        c = a & b
        a = a ^ b
        b = c << 1
    return a & 0xffffffff if b > 0xffffffff else a

# List Functions
def getSum(a,b):
    return sum([a, b])
