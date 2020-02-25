# https://leetcode.com/problems/group-anagrams/
# 49. Group Anagrams
# Given an array of strings, group anagrams together.
# Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
# All inputs will be in lowercase.
# The order of your output does not matter.

def groupAnagrams(strs):
    d = {}
    for s in strs:
        sort_s = ''.join(sorted(s))
        if sort_s not in d:
            d[sort_s] = []
        d[sort_s].append(s)
    return d.values()
