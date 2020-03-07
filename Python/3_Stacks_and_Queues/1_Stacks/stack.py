def sortStack(stack):
    tempstack = []
    while stack:
        temp = stack.pop()
        while tempstack and tempstack[-1] > temp:
            stack.append(tempstack.pop())
        tempstack.append(temp)
    return tempstack

def reverseStack(stack):
    def insertAtBottom(stack, x):
        if not stack:
            stack.append(x)
        else:
            temp = stack.pop()
            insertAtBottom(stack, x)
            stack.append(temp)
    if stack:
        temp = stack.pop()
        reverseStack(stack)
        insertAtBottom(stack, temp)
