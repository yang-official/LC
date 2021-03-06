# https://leetcode.com/problems/string-without-aaa-or-bbb/
# Given two integers A and B, return any string S such that:
#     S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
#     The substring 'aaa' does not occur in S;
#     The substring 'bbb' does not occur in S.
# Example 1:
# Input: A = 1, B = 2
# Output: "abb"
# Explanation: "abb", "bab" and "bba" are all correct answers.
# Example 2:
# Input: A = 4, B = 1
# Output: "aabaa"
# Note:
#     0 <= A <= 100
#     0 <= B <= 100
#     It is guaranteed such an S exists for the given A and B.

def strWithout3a3b(A, B):
    if (B <= A < 2 * B):
        return "aab" * (A - B) + "ab" * (2 * B - A);
    elif(2 * B <= A <= 2 * B + 2):
        return "aab" * B + "a" * (A - B * 2);
    elif(A < B < 2 * A):
        return "bba" * (B - A) + "ba" * (2 * A - B); 
    elif(2 * A <= B <= 2 * A + 2):
        return "bba" * A + "b" * (B - A * 2);
    else:
        return "";
