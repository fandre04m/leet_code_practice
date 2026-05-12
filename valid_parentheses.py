string = "([{}])"

def validate_pairs_brute(string: str) -> bool:
    to_remove = "(){}[]"
    ret = ""
    for ch in string:
        if ch in to_remove:
            ret += ch
    while "()" in ret or "[]" in ret or "{}" in ret:
        ret = ret.replace("[]", "")
        ret = ret.replace("()", "")
        ret = ret.replace("{}", "")
    return ret == ""


def validate_pairs_stack(string: str) -> bool:
    to_remove = "(){}[]"
    clean_str = ""
    for ch in string:
        if ch in to_remove:
            clean_str += ch

    stack = []
    closed_to_open = {")": "(", "]": "[", "}": "{"}
    for ch in clean_str:
        if ch in closed_to_open:
            if stack and stack[-1] == closed_to_open[ch]:
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)

    return True if not stack else False


print(f"Using brute force: {validate_pairs_brute(string)}")
print(f"Using stack: {validate_pairs_stack(string)}")