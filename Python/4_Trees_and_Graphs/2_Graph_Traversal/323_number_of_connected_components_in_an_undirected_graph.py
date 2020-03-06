# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
#  Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.
# Example 1:
#      0          3
#      |          |
#      1 --- 2    4
# Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.
# Example 2:
#      0           4
#      |           |
#      1 --- 2 --- 3
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.
# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

def countComponents(n, edges):
    if n == 0:
        return 0
    if n <= 1:
        return 1
    def _find(x):
        while x != UF[x]:
            UF[x] = UF[UF[x]]
            x = UF[UF[x]]
        return x
    UF = [i for i in range(n)]
    result = n
    for x, y in edges:
        if UF[find(x)] != UF[find(y)]:
            result -= 1
            UF[find(x)] = UF[find(y)]
    return result
