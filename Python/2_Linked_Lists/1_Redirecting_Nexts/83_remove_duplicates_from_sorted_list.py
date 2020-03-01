# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# 83. Remove Duplicates from Sorted List
# Given a sorted linked list, delete all duplicates such that each element appear only once.
# Example 1:
# Input: 1->1->2
# Output: 1->2
# Example 2:
# Input: 1->1->2->3->3
# Output: 1->2->3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def deleteDuplicates(head):
    if head is None:
        return
    curr = head
    while curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

# Variant, unsorted linked list
def deleteDuplicatesUnsorted(head):
    if head is None:
        return
    seen = set()
    curr = head
    while curr.next:
        seen.add(curr.val)
        if curr.next.val in seen:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
