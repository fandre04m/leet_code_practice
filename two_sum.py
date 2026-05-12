#!/usr/bin/env python3

nums, target = [0, 3, 4, 8], 7


def find_indexes_brute(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return [0, 0]


def find_indexes_hash(nums: list[int], target: int) -> list[int]:
    indexes = {}  # num, index

    for i, num in enumerate(nums):
        diff = target - num
        if diff in indexes:
            return [indexes[diff], i]
        indexes[num] = i
    return []


if __name__ == "__main__":
    print(f"Using brute force: {find_indexes_brute(nums, target)}")
    print(f"Using hash: {find_indexes_hash(nums, target)}")
