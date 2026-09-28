# Time: O(n), Space: O(n)
# Stretch Goal Included: Returns index of first mismatched bracket, or -1 if balanced.

def is_balanced(s: str) -> bool:
    """Base requirement: returns True if brackets are balanced, False otherwise."""
    return is_balanced_stretch(s) == -1


def is_balanced_stretch(s: str) -> int:
    """Stretch Goal: Returns the 0-based index of the first mismatched bracket,
    or -1 if the string is balanced.
    """
    stack = []  # Stores tuples of (bracket_char, index)
    matching = {")": "(", "]": "[", "}": "{"}
    openers = set(matching.values())

    for idx, char in enumerate(s):
        if char in openers:
            stack.append((char, idx))
        elif char in matching:
            if not stack or stack[-1][0] != matching[char]:
                return idx
            stack.pop()

    if stack:
        return stack[0][1]

    return -1


if __name__ == "__main__":
    # Test Case 1: Standard balanced string with non-bracket characters
    assert is_balanced("(a[b]{c})") == True
    assert is_balanced_stretch("(a[b]{c})") == -1

    # Test Case 2: Mismatched closing bracket
    assert is_balanced("([)]") == False
    assert is_balanced_stretch("([)]") == 2

    # Test Case 3: Edge cases (empty string and unmatched opening brackets)
    assert is_balanced("") == True
    assert is_balanced("((") == False
    assert is_balanced_stretch("((") == 0
    print("Challenge 1 tests passed!")
