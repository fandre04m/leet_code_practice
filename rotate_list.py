# Write a function that rotates an array to the right by k positions,
#   rotating right by k means the last k elements move to the front.


num_array = [0, 1, 2, 3, 4]


def rotate_list_concat(array: list[int], times: int) -> list[int]:
    if not array:
        return []
    times %= len(array)
    rot_arr = array[-times:] + array[:-times]
    return rot_arr


def rotate_list_pop(array: list[int], times: int) -> list[int]:
    if not array:
        return []
    for _ in range(times):
        num = array.pop()
        array.insert(0, num)
    return array


print(f"Using concatenation: {rotate_list_concat(num_array, 2)}")
print(f"Using pop: {rotate_list_pop(num_array, 7)}")
