# Time: Amortized O(1) append, O(1) get/set, Space: O(n)

import ctypes

class DynamicArray:
    def __init__(self, initial_capacity: int = 2):
        self.size = 0
        self.capacity = initial_capacity
        self.array = self._make_array(self.capacity)

    def _make_array(self, cap: int):
        return (cap * ctypes.py_object)()

    def _resize(self, new_cap: int):
        new_arr = self._make_array(new_cap)
        for i in range(self.size):
            new_arr[i] = self.array[i]
        self.array = new_arr
        self.capacity = new_cap

    def append(self, x) -> None:
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.size] = x
        self.size += 1

    def get(self, i: int):
        if not (0 <= i < self.size):
            raise IndexError("Index out of bounds")
        return self.array[i]

    def set(self, i: int, x) -> None:
        if not (0 <= i < self.size):
            raise IndexError("Index out of bounds")
        self.array[i] = x

    def remove(self, i: int):
        """Stretch Goal: Deletes element at index i and shrinks if capacity usage < 25%."""
        if not (0 <= i < self.size):
            raise IndexError("Index out of bounds")

        val = self.array[i]
        for j in range(i, self.size - 1):
            self.array[j] = self.array[j + 1]
        self.size -= 1

        if self.size > 0 and self.size <= self.capacity // 4:
            new_cap = max(2, self.capacity // 2)
            if new_cap != self.capacity:
                self._resize(new_cap)
        return val


if __name__ == "__main__":
    da = DynamicArray(initial_capacity=2)

    # Test Case 1: Appends triggering automatic doubling resize
    da.append(10)
    da.append(20)
    assert da.capacity == 2
    da.append(30)
    assert da.capacity == 4
    assert da.get(2) == 30

    # Test Case 2: Set and Get functionality
    da.set(0, 99)
    assert da.get(0) == 99

    # Test Case 3: Bounds checking error and Stretch Shrinking check
    try:
        da.get(5)
        assert False
    except IndexError:
        assert True

    da.remove(0)
    da.remove(0)
    assert da.size == 1
    print("Challenge 7 tests passed!")
