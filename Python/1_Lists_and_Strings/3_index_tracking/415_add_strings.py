# https://leetcode.com/problems/add-strings/
# Given two non-negative integers num1 and num2 represented as string,
# return the sum of num1 and num2.
# Note:
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


def addStrings(num1, num2):
    num1 = num1[::-1]
    num2 = num2[::-1]
    i = 0
    carry = 0
    result = ""
    while i < len(num1) and i < len(num2):
        total = int(num1[i]) + int(num2[i]) + carry
        carry = total // 10
        result += str(total % 10)
        i += 1
    if i < len(num1):
        while i < len(num1):
            total = int(num1[i]) + carry
            carry = total // 10
            result += str(total % 10)
            i += 1
    elif i < len(num2):
        while i < len(num2):
            total = int(num2[i]) + carry
            carry = total // 10
            result += str(total % 10)
            i += 1
    if carry != 0:
        result += str(carry)
    return result[::-1]

# Comment:
# See also LC 2 Add Two Numbers
