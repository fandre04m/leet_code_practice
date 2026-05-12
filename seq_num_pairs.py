"""
5. Count Sequential Numeric Pairs

Given a string s, count how many times two consecutive characters are numeric and sequential in increasing order.

Example:

Input:
"1234"

Output:
3

Explanation:

1 -> 2
2 -> 3
3 -> 4
"""

s = "1234ab4576589"

def check_sequence(s: str) -> int:
    counter = 0
    for i in range(1, len(s)):
        if s[i].isdigit() and s[i - 1].isdigit():
            if int(s[i]) == int(s[i - 1]) + 1:
                counter += 1
    return counter


print(check_sequence(s))