# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# 19. Remove Nth Node From End of List
# Given a linked list, remove the n-th node from the end of list and return its head.
# Example:
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Follow up:
# Could you do this in one pass?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def removeNthFromEnd(head, n):
    slow = fast = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

# Variant, find the kth to last
def findKthFromEnd(head, k):
    slow = fast = head
    for _ in range(k):
        fast = fast.next
    if not fast:
        return slow
    while fast.next:
        fast = fast.next
        slow = slow.next
    return slow.next
