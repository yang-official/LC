# https://leetcode.com/problems/design-circular-queue/
# 622. Design Circular Queue
# Design your implementation of the circular queue. The circular queue is a
# linear data structure in which the operations are performed based on FIFO
# (First In First Out) principle and the last position is connected back to
# the first position to make a circle. It is also called "Ring Buffer".
# One of the benefits of the circular queue is that we can make use of the
# spaces in front of the queue. In a normal queue, once the queue becomes full,
# we cannot insert the next element even if there is a space in front of the queue.
# But using the circular queue, we can use the space to store new values.
# Your implementation should support following operations:
#     MyCircularQueue(k): Constructor, set the size of the queue to be k.
#     Front: Get the front item from the queue. If the queue is empty, return -1.
#     Rear: Get the last item from the queue. If the queue is empty, return -1.
#     enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
#     deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
#     isEmpty(): Checks whether the circular queue is empty or not.
#     isFull(): Checks whether the circular queue is full or not.
# Example:
# MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be 3
# circularQueue.enQueue(1);  // return true
# circularQueue.enQueue(2);  // return true
# circularQueue.enQueue(3);  // return true
# circularQueue.enQueue(4);  // return false, the queue is full
# circularQueue.Rear();  // return 3
# circularQueue.isFull();  // return true
# circularQueue.deQueue();  // return true
# circularQueue.enQueue(4);  // return true
# circularQueue.Rear();  // return 4
# Note:
#     All values will be in the range of [0, 1000].
#     The number of operations will be in the range of [1, 1000].
#     Please do not use the built-in Queue library.

class MyCircularQueue:

    def __init__(self, k: int): # Intialize, set size of queue to be k
        self.data = [None] * k
        self.max = k
        self.size = 0
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool: # Insert, return true if successful
        if self.isFull():
            return False
        self.front = (self.front + 1) % self.max
        self.data[self.front] = value
        self.size += 1
        return True

    def deQueue(self) -> bool: # Delete, return true if successful
        if self.isEmpty():
            return False
        self.rear = (self.rear + 1) % self.max
        self.data[self.rear] = None
        self.size -= 1
        return True

    def Front(self) -> int: # Get front item
        if self.isEmpty():
            return -1
        return self.data[(self.rear + 1) % self.max]

    def Rear(self) -> int: # Get last item
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def isEmpty(self) -> bool: # check if queue is empty
        return self.size == 0

    def isFull(self) -> bool: # check if queue is full
        return self.size == self.max
