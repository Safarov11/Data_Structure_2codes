# Time: Amortized O(1) per operation, Space: O(n)
# Stretch Goal Included: Potential function proof.

"""
STRETCH GOAL PROOF (Potential Function Method):
Let Phi be the potential function defined as:
    Phi = 2 * len(self.in_stack)

- Enqueue(x):
  Actual cost c = 1.
  Delta_Phi = Phi_after - Phi_before = 2 * (len(in) + 1) - 2 * len(in) = 2.
  Amortized cost = c + Delta_Phi = 1 + 2 = 3 = O(1).

- Dequeue():
  Case 1: out_stack is non-empty.
    Actual cost c = 1. Delta_Phi = 0. Amortized cost = 1 = O(1).
  Case 2: out_stack is empty and len(in_stack) = k.
    Actual cost c = k (pours elements) + 1 (pop) = k + 1.
    Delta_Phi = 0 (len(in) becomes 0) - 2 * k = -2k.
    Amortized cost = (k + 1) + (-2k) = 1 - k <= 1 = O(1).

Therefore, all operations run in amortized O(1) time.
"""


class QueueFromStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x) -> None:
        self.in_stack.append(x)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            raise IndexError("dequeue from empty queue")
        return self.out_stack.pop()


if __name__ == "__main__":
    q = QueueFromStacks()

    # Test Case 1: Basic FIFO order
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2

    # Test Case 2: Interleaved enqueue and dequeue
    q.enqueue(4)
    assert q.dequeue() == 3
    assert q.dequeue() == 4

    # Test Case 3: Empty queue error handling (edge case)
    try:
        q.dequeue()
        assert False, "Should have raised IndexError"
    except IndexError:
        assert True
    print("Challenge 4 tests passed!")
