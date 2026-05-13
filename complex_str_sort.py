# Write a function that sorts a list of strings according to multiple criteria:
#
# 1. Primary sort: By string length (shortest first)
#
# 2. Secondary sort: ASCII order, except letters are
#   compared case-insensitively (for strings of same length)
#
# 3. Tertiary sort: By number of vowels
#   (ascending, for same length and lexically equal)
#
# 4. Equal strings will appear in the same order as in the input list.


str_lst = ["fabio", "maximiano", "tatiana", "ahh", "a", "z"]


def vowel_counter(s: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)


def sort_key(s: str) -> tuple:
    return (len(s), s.lower(), vowel_counter(s))


def list_sorter(str_lst: list[str]) -> list[str]:
    return sorted(str_lst, key=sort_key)


print(list_sorter(str_lst))
