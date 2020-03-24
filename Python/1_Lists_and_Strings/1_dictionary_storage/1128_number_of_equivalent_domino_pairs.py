# https://leetcode.com/problems/number-of-equivalent-domino-pairs/
# 1128. Number of Equivalent Domino Pairs
# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.
# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].
# Example 1:
# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
# Constraints:
#     1 <= dominoes.length <= 40000
#     1 <= dominoes[i][j] <= 9

def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
    seen = {}
    for d in dominoes:
        x = tuple(sorted(d))
        if x not in seen:
            seen[x] = 0
        seen[x] += 1
    pairs = 0
    for n in seen.values():
        pairs += n*(n-1)//2
    return pairs
