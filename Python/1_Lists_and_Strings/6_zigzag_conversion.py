# https://leetcode.com/problems/zigzag-conversion/
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

def convert(s, numRows):
    if len(s) <= 1 or numRows == 1:
        return s
    res = [''] * numRows
    periodic = 2 * numRows - 2
    for i in range(len(s)):
        index = i % periodic
        if index <= numRows - 1:
            res[index] += s[i]
        else:
            index = periodic - index
            res[index] += s[i]
    return ''.join(res)
