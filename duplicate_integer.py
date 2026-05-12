#!/usr/bin/env python3

num_array = [-24, -11, 0, 0, 3, 42, 54]


def has_duplicate_brute(array: list[int]) -> bool:
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                return True
    return False


def has_duplicate_hash(array: list[int]) -> bool:
    seen = set()

    for num in array:
        if num in seen:
            return True
        seen.add(num)
    return False


def has_duplicate_len(array: list[int]) -> bool:
    return len(set(array)) < len(array)


def has_duplicate_sort(array: list[int]) -> bool:
    sorted_array = sorted(array)
    for num in range(1, len(sorted_array)):
        if sorted_array[num] == sorted_array[num - 1]:
            return True
    return False


if __name__ == "__main__":
    print(f"Using brute force: {has_duplicate_brute(num_array)}")
    print(f"Using hash: {has_duplicate_hash(num_array)}")
    print(f"Using lenght: {has_duplicate_len(num_array)}")
    print(f"Using sort: {has_duplicate_sort(num_array)}")