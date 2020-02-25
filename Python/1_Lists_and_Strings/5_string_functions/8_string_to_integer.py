# https://leetcode.com/problems/string-to-integer-atoi/
# Implement atoi which converts a string to an integer.
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
# If no valid conversion could be performed, a zero value is returned.

def myAtoi(str):
    num = ''
    str = str.lstrip(' ')
    if (not str):
        return 0
    if (str[0] == '-' or str[0] == '+'):
        num = str[0]
        str = str[1:]
    for ch in str:
        if (ch.isdigit()):
            num += ch
        else:
            break
    try:
        value = int(num)
        if (value.bit_length() >= 32):
            return (2**31-1) if value > 0 else -2**31
        return value
    except ValueError:
        return 0
