# https://leetcode.com/problems/reorganize-string/
# 767. Reorganize String
# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
# If possible, output any possible result.  If not possible, return the empty string.
# Example 1:
# Input: S = "aab"
# Output: "aba"
# Example 2:
# Input: S = "aaab"
# Output: ""
# Note:
#     S will consist of lowercase letters and have length in range [1, 500].

def reorganizeString(self, S: str) -> str:
    if not S:
        return ""
    d = {}
    for c in S:
        if c not in d:
            d[c] = 0
        d[c] += 1
    h = []
    from heapq import heappush, heappop
    for k in d:
        heappush(h, (-d[k], k))
    res = ""
    while len(h) > 1:
        f1, c1 = heappop(h)
        f2, c2 = heappop(h)
        res += c1
        res += c2
        if abs(f1) > 1:
            heappush(h, (f1+1, c1))
        if abs(f2) > 1:
            heappush(h, (f2+1, c2))
    if len(h) > 0:
        f, c = h[0]
        if abs(f) > 1:
            return ""
        else:
            res += c
    return res
