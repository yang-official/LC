# https://leetcode.com/problems/implement-stack-using-queues/
# 225. Implement Stack using Queues

# Implement the following operations of a stack using queues.
#     push(x) -- Push element x onto stack.
#     pop() -- Removes the element on top of the stack.
#     top() -- Get the top element.
#     empty() -- Return whether the stack is empty.
# Example:
# MyStack stack = new MyStack();
# stack.push(1);
# stack.push(2);
# stack.top();   // returns 2
# stack.pop();   // returns 2
# stack.empty(); // returns false
# Notes:
#     You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
#     Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
#     You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        self._top = None

    def push(self, x: int) -> None:
        self.queue1.append(x)
        self._top = x


    def pop(self) -> int:
        while len(self.queue1) > 1:
            self._top = self.queue1.pop(0)
            self.queue2.append(self._top)
        result = self.queue1.pop(0)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return result

    def top(self) -> int:
        return self._top


    def empty(self) -> bool:
        return len(self.queue1 == 0) and len(self.queue2 == 0)
