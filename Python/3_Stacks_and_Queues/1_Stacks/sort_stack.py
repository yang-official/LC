def sortStack(stack):
    tempstack = []
    while stack:
        temp = stack.pop()
        while tempstack and tempstack[-1] > temp:
            stack.append(tempstack.pop())
        tempstack.append(temp)
    return tempstack
