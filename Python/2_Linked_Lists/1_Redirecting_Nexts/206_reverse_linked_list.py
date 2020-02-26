# https://leetcode.com/problems/reverse-linked-list/
# 206. Reverse Linked List
# Reverse a singly linked list.
# Example:
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:
# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Iterative
def reverseList(head):
    prev, curr = None, head
    while curr:
        nex = curr.next
        curr.next = prev
        prev, curr = curr, nex
    return prev

# Recursive
def reverseList(head):
    if not head or not head.next:
        return head
    node = reverseList(head.next)
    head.next.next = head
    head.next = None
    return node
