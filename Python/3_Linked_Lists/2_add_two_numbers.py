# https://leetcode.com/problems/add-two-numbers/

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def addTwoNumbers(l1, l2):
    head = result = ListNode(0)
    carry = 0
    while l1 or l2:
        if not l1:
            l1 = ListNode(0)
        if not l2:
            l2 = ListNode(0)
        total = l1.val + l2.val + carry
        result.next = ListNode(total % 10)
        carry = total // 10
        l1 = l1.next
        l2 = l2.next
        result = result.next
    if carry > 0:
        result.next = ListNode(carry)
    return head.next
