# Given a string s, return true if it is a palindrome, otherwise return false.
#
# A palindrome is a string that reads the same forward and backward.
# It is also case-insensitive and ignores all non-alphanumeric characters.
#
# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9)


def is_palindrome_brute(s: str) -> bool:
    clean_str = ""
    for ch in s:
        if ch.isalpha() or ch.isdigit():
            clean_str += ch.lower()
    return clean_str == clean_str[::-1]


def is_palindrome_pointers(s: str) -> bool:
    b = 0
    e = len(s) - 1

    while b < e:
        while b < e and not s[b].isalnum():
            b += 1
        while e > b and not s[e].isalnum():
            e -= 1
        if s[b].lower() != s[e].lower():
            return False
        b += 1
        e -= 1
    return True


print(f"Using brute force: {is_palindrome_brute('girafarig?')}")
print(f"Using pointers: {is_palindrome_pointers('Girafa rig?')}")
