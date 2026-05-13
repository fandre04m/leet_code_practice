""" 
Given a list of strings, sort the list using these rules:

Shorter strings come first.
If two strings have the same length, sort them alphabetically.

Return the sorted list.

Example:

Input:
["abc", "a", "ab", "aaa", "b"]

Output:
["a", "b", "ab", "aaa", "abc"] 
"""

lst = ["abc", "a", "bb", "ab", "aaa", "b"]


def sort_strings(str_lst: list[str]) -> list[str]:
    return sorted(str_lst, key=lambda string: (len(string), string))


print(sort_strings(lst))
