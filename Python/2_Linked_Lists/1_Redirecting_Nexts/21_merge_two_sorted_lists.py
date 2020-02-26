# https://leetcode.com/problems/merge-two-sorted-lists/
# 21. Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
# Example:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def mergeTwoLists(l1, l2):
    head = node = ListNode(None)
    while l1 or l2:
        if not l1:
            node.next = l2
            break
        elif not l2:
            node.next = l1
            break
        if l1.val < l2.val:
            node.next = l1
            l1 = l1.next
            node = node.next
        elif l1.val >= l2.val:
            node.next = l2
            l2 = l2.next
            node = node.next
    return head.next
