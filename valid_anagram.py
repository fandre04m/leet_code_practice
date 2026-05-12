#!/usr/bin/env python3

s1 = "racecar"
s2 = "carrace"

def is_anagram_sort(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    if sorted_s1 == sorted_s2:
        return True
    return False


def is_anagram_dict(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    freq_1, freq_2 = {}, {}
    for char in range(len(s1)):
        freq_1[s1[char]] = 1 + freq_1.get(s1[char], 0)
        freq_2[s2[char]] = 1 + freq_2.get(s2[char], 0)
    return freq_1 == freq_2


if __name__ == "__main__":
    print(f"Using sort: {is_anagram_sort(s1, s2)}")
    print(f"Using dictionaries: {is_anagram_dict(s1, s2)}")