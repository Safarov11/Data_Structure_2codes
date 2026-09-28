# Time: O(1) worst-case for all ops, Space: O(n)

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        current_min = min(x, self.min_stack[-1]) if self.min_stack else x
        self.min_stack.append(current_min)

    def pop(self) -> int:
        if not self.stack:
            raise IndexError("pop from empty stack")
        self.min_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            raise IndexError("top from empty stack")
        return self.stack[-1]

    def get_min(self) -> int:
        if not self.min_stack:
            raise IndexError("get_min from empty stack")
        return self.min_stack[-1]


class MinStackOptimized:
    """Stretch Goal: Space-optimized stack storing relative deltas."""

    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_val = x
        else:
            delta = x - self.min_val
            self.stack.append(delta)
            if delta < 0:
                self.min_val = x

    def pop(self) -> int:
        if not self.stack:
            raise IndexError("pop from empty stack")
        diff = self.stack.pop()
        if diff < 0:
            val = self.min_val
            self.min_val = self.min_val - diff
            return val
        else:
            return self.min_val + diff

    def top(self) -> int:
        if not self.stack:
            raise IndexError("top from empty stack")
        diff = self.stack[-1]
        return self.min_val if diff < 0 else self.min_val + diff

    def get_min(self) -> int:
        if self.min_val is None:
            raise IndexError("get_min from empty stack")
        return self.min_val


if __name__ == "__main__":
    # Test Case 1: Standard operation order
    ms = MinStack()
    ms.push(3)
    ms.push(5)
    ms.push(2)
    assert ms.get_min() == 2
    ms.pop()
    assert ms.get_min() == 3
    assert ms.top() == 5

    # Test Case 2: Optimized delta-stack implementation
    opt_ms = MinStackOptimized()
    opt_ms.push(3)
    opt_ms.push(5)
    opt_ms.push(2)
    assert opt_ms.get_min() == 2
    assert opt_ms.pop() == 2
    assert opt_ms.get_min() == 3

    # Test Case 3: Empty stack exception check
    empty_ms = MinStack()
    try:
        empty_ms.pop()
        assert False
    except IndexError:
        assert True
    print("Challenge 6 tests passed!")
