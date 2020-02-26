# https://leetcode.com/problems/valid-parentheses/
# 20. Valid Parentheses
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
# Example 1:
# Input: "()"
# Output: true
# Example 2:
# Input: "()[]{}"
# Output: true
# Example 3:
# Input: "(]"
# Output: false
# Example 4:
# Input: "([)]"
# Output: false
# Example 5:
# Input: "{[]}"
# Output: true

def isValid(s):
    stack = []
    d = {'(':')','{':'}','[':']'}
    for e in s:
        if e in d.values():
            if len(stack) == 0:
                return False
            c = stack.pop()
            if d[c] != e:
                return False
        else:
            stack.append(e)
    return len(stack) == 0

# optimized by left check first
def isValid(s):
    stack = []
    bracket = {'(': ')','[': ']','{': '}'}
    for item in s:
        if item in bracket:
            stack.append(bracket[item])
        elif not stack or stack.pop() != item:
            return False
    return len(stack) == 0
