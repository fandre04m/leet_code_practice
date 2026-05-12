"""
6. Merge Two Sorted Lists

Given two sorted integer lists, merge them into a single sorted list.

Return the merged list.

Example:

Input:
lst1 = [1, 3, 5]
lst2 = [2, 4, 6]

Output:
[1, 2, 3, 4, 5, 6]
"""

lst_1 = [10, 20, 30]
lst_2 = [1, 2, 3]

lst_3 = [1, 2, 3]
lst_4 = [3, 4, 5]

def merge_lists_no_repeat(lst1: list[int], lst2: list[int]) -> list[int]:
    return sorted(set(lst1 + lst2))


def merge_lists_with_repeat(lst1: list[int], lst2: list[int]) -> list[int]:
    return sorted(lst1 + lst2)


print(f"With no repeats: {merge_lists_no_repeat(lst_1, lst_2)}")
print(f"With repeats: {merge_lists_with_repeat(lst_3, lst_4)}")