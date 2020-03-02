# https://leetcode.com/problems/broken-calculator/
# On a broken calculator that has a number showing on its display, we can perform two operations:
#     Double: Multiply the number on the display by 2, or;
#     Decrement: Subtract 1 from the number on the display.
# Initially, the calculator is displaying the number X.
# Return the minimum number of operations needed to display the number Y.
# Example 1:
# Input: X = 2, Y = 3
# Output: 2
# Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
# Example 2:
# Input: X = 5, Y = 8
# Output: 2
# Explanation: Use decrement and then double {5 -> 4 -> 8}.
# Example 3:
# Input: X = 3, Y = 10
# Output: 3
# Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.
# Example 4:
# Input: X = 1024, Y = 1
# Output: 1023
# Explanation: Use decrement operations 1023 times.

def brokenCalc(X, Y):
    if X > Y or X == Y:
        return X - Y
    count = 0
    while Y > X:
        if Y % 2 == 0:
            count += 1
            Y //= 2
        if Y <= X:
            return count + (X - Y)
        if Y % 2 != 0:
            count += 1
            Y += 1
    return count
