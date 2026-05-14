"""
4. Rotate Alphabetical Characters

Given a string s and an integer times,
    rotate each alphabetical character forward in the alphabet by times.

Preserve uppercase/lowercase.
Wrap around alphabetically.
Non-alphabetical characters remain unchanged.

Example:

Input:
"abc", 3

Output:
"def"
"""

to_rotate = "abc abc! --It works! zzz"


def rotate_char(s: str, times: int) -> str:
    new_str = ""
    for ch in s:
        if ch.islower():
            base = ord("a")
            new_str += chr((ord(ch) - base + times) % 26 + base)
        elif ch.isupper():
            base = ord("A")
            new_str += chr((ord(ch) - base + times) % 26 + base)
        else:
            new_str += ch
    return new_str


print(rotate_char(to_rotate, 3))
