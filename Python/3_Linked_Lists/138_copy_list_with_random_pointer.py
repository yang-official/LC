# https://leetcode.com/problems/copy-list-with-random-pointer/
# A linked list is given such that each node contains an additional random pointer
# which could point to any node in the list or null.
# Return a deep copy of the list.
# The Linked List is represented in the input/output as a list of n nodes.
# Each node is represented as a pair of [val, random_index] where:
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random pointer points to,
# or null if it does not point to any node.

def copyRandomList(head):
    d = {}
    prev, curr = None, head
    while curr:
        if curr not in d:
            d[curr] = Node(curr.val, curr.next, curr.random)
        if prev:
            prev.next = d[curr]
        else:
            head = d[curr]
        if curr.random:
            if curr.random not in d:
                d[curr.random] = Node(curr.random.val, curr.random.next, curr.random.random)
            d[curr].random = d[curr.random]
        prev, curr = d[curr], curr.next
    return head
