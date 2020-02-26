# https://leetcode.com/problems/merge-k-sorted-lists/
# 23. Merge k Sorted Lists
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
# Example:
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def mergeKLists(lists):
    if not lists:
        return None
    d = {}
    for node in lists:
        while node:
            if node.val not in d:
                d[node.val] = [node]
            else:
                d[node.val].append(node)
            node = node.next
    keys = list(d.keys())
    keys = sorted(keys)
    merge = ListNode(0)
    p = merge
    for key in keys:
        for node in d.get(key):
            p.next = node
            p = p.next
    return merge.next
