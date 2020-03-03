# https://leetcode.com/problems/palindrome-linked-list/
# 234. Palindrome Linked List
# Given a singly linked list, determine if it is a palindrome.
# Example 1:
# Input: 1->2
# Output: false
# Example 2:
# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# unoptimized O(N) space
def isPalindrome(head):
    l = []
    while head:
        l.append(head.val)
        head = head.next
    return l == l[::-1]

# optmized O(1) space using fast and slow pointers, reverse first half of list while scanning
def isPalindrome(head):
    if not head or not head.next:
        return True
    fast, slow = head, head
    mid = None
    while fast.next and fast.next.next:
        fast = fast.next.next
        temp, mid = mid, slow
        slow = slow.next
        mid.next = temp
    l2 = slow.next
    if fast.next:
        slow.next = mid
        l1 = slow
    else:
        l1 = mid
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1, l2 = l1.next, l2.next
    return not l1 and not l2
