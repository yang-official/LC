# Write a function that returns the elements on odd positions (0 based) in a list
def solution(input):
    output = []
    for i, e in enumerate(input):
        if i % 2 != 0:
            output.append(e)
    return output
assert solution([0,1,2,3,4,5]) == [1,3,5]
assert solution([1,-1,2,-2]) == [-1,-2]

# Write a function that returns the cumulative sum of elements in a list
def solution(input):
    cumsum = 0
    output = []
    for e in input:
        cumsum += e
        output.append(cumsum)
    return output
assert solution([1,1,1]) == [1,2,3]
assert solution([1,-1,3]) == [1,0,3]

# Write a function that takes a number and returns a list of its digits
def solution(input):
    output = []
    for e in str(input):
        output.append(int(e))
    return output
assert solution(123) == [1,2,3]
assert solution(400) == [4,0,0]

# Return the "centered" average of an array of ints,
# which we'll say is the mean average of the values,
# except ignoring the largest and smallest values in the array.
# If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value.
# Use int division to produce the final average. You may assume that the array is length 3 or more.
def solution(input):
    n = len(input)
    total = sum(input)
    return (total - max(input) - min(input)) // (n - 2)
assert solution([1, 2, 3, 4, 100]) == 3
assert solution([1, 1, 5, 5, 10, 8, 7]) == 5
assert solution([-10, -4, -2, -4, -2, 0]) == -3
