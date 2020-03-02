# https://leetcode.com/problems/generate-parentheses/
# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# For example, given n = 3, a solution set is:
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

# Recursive
def generateParenthesis(n):
    if n == 1:
        return ["()"]
    prev, vals = generateParenthesis(n-1), set()
    for v in prev:
        for i in range(len(prev[0]) + 1):
            vals.add(v[:i] + "()" + v[i:])
    return list(vals)

# Iterative
def generateParenthesis(n):
    if n == 0:
        return [""]
    result = ["()"]
    for _ in range(1, n):
        temp = []
        for r in result:
            for i in range(len(r)):
                temp.append(r[:i] + '()' + r[i:])
        result = list(set(temp))
    return result
