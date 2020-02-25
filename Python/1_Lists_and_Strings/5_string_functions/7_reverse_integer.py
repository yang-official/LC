# https://leetcode.com/problems/reverse-integer/
# 7. Reverse Integer
# Given a 32-bit signed integer, reverse digits of an integer.
# Example 1:
# Input: 123
# Output: 321
# Example 2:
# Input: -123
# Output: -321
# Example 3:
# Input: 120
# Output: 21

def reverse(x):
    if x == 0:
        return 0
    x_list = list(str(x))
    x_list.reverse()
    if x_list[-1] == '-':
        x_list.pop()
        x_list.insert(0,'-')
    r = int(''.join(x_list))
    if (-2**31 > r or r > 2**31-1):
        return 0
    else:
        return r
