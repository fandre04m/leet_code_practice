# Assignment
#
# Write a function that converts a number from one base to another.
# Support bases from 2 to 36 inclusive, using digits 0-9
#   and letters A-Z for values 10-35.
# Return "ERROR" for invalid inputs (base, digits)
#
# Examples:
#
# Input
# number_base_converter("1010", 2, 10)
# Output
# "10"
#
# Input
# number_base_converter("FF", 16, 10)
# Output
# "255"
#
# Input
# number_base_converter("255", 10, 16)
# Output
# "FF"
#
# Function signature:
# def number_base_converter(number: str, from_base: int, to_base: int) -> str:


def convert_to_base(num: int, base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num == 0:
        return "0"

    result = ""
    while num > 0:
        result = digits[num % base] + result
        num = num // base

    return result


def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if to_base < 2 or to_base > 36:
        return "ERROR"
    negative = False
    if number.startswith("-"):
        negative = True
        number = number.lstrip("-")
    try:
        base_num = int(number, from_base)
    except ValueError:
        return "ERROR"
    res = convert_to_base(base_num, to_base)
    if negative:
        res = "-" + res
    return res


print(number_base_converter("1Z", 36, 10))
