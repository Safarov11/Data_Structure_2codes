# Time: O(log n), Space: O(1)

def search_range(nums: list[int], target: int) -> tuple[int, int]:
    """Base requirement: Finds the lower and upper bounds of target in O(log n)."""

    def find_bound(find_first: bool) -> int:
        left, right = 0, len(nums) - 1
        bound = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                bound = mid
                if find_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return bound

    first = find_bound(find_first=True)
    if first == -1:
        return (-1, -1)
    last = find_bound(find_first=False)
    return (first, last)


def count_occurrences(nums: list[int], target: int) -> int:
    """Stretch Goal: Counts occurrences of target in O(log n) time."""
    first, last = search_range(nums, target)
    if first == -1:
        return 0
    return last - first + 1


if __name__ == "__main__":
    # Test Case 1: Standard case with multiple target occurrences
    nums1 = [5, 7, 7, 8, 8, 8, 10]
    assert search_range(nums1, 8) == (3, 5)
    assert count_occurrences(nums1, 8) == 3

    # Test Case 2: Target not found
    assert search_range(nums1, 6) == (-1, -1)
    assert count_occurrences(nums1, 6) == 0

    # Test Case 3: Single element matching target and empty array (edge cases)
    assert search_range([8], 8) == (0, 0)
    assert search_range([], 5) == (-1, -1)
    print("Challenge 9 tests passed!")
