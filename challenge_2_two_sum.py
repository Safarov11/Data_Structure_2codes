# Time: O(n), Space: O(n)
# Stretch Goal Included: Finds all unique index pairs summing to target.

def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    """Base requirement: Single pass solution assuming exactly one valid pair."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    raise ValueError("No solution found")


def two_sum_stretch(nums: list[int], target: int) -> list[tuple[int, int]]:
    """Stretch Goal: Returns all index pairs that sum to target."""
    val_to_indices = {}
    for idx, val in enumerate(nums):
        val_to_indices.setdefault(val, []).append(idx)

    pairs = []
    used_indices = set()

    for i, x in enumerate(nums):
        if i in used_indices:
            continue
        complement = target - x
        if complement in val_to_indices:
            for j in val_to_indices[complement]:
                if j > i and j not in used_indices:
                    pairs.append((i, j))
                    used_indices.add(i)
                    used_indices.add(j)
                    break

    return pairs


if __name__ == "__main__":
    # Test Case 1: Standard positive integers
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)

    # Test Case 2: Negative numbers and zero
    assert two_sum([-3, 4, 3, 90], 0) == (0, 2)

    # Test Case 3: Stretch goal with duplicate values
    assert two_sum_stretch([2, 7, 2, 7], 9) == [(0, 1), (2, 3)]
    print("Challenge 2 tests passed!")
