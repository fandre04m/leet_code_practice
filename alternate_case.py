"""
2. Alternate Character Case

Given a string s, convert only alphabetical characters in sequential alternating format:

first alphabetical character -> uppercase
second alphabetical character -> lowercase
third alphabetical character -> uppercase
etc.

Non-alphabetical characters remain unchanged and do not affect the sequence.

Example:

Input:
"hello world!"

Output:
"HeLlO wOrLd!"
"""

string = "hello world!"


def alternator(string: str) -> str:
    counter = 0
    alt_str = ""

    for ch in string:
        if ch.isalpha():
            if counter % 2 == 0:
                alt_str += ch.upper()
            else:
                alt_str += ch.lower()
            counter += 1
        else:
            alt_str += ch
    return alt_str


print(alternator(string))
