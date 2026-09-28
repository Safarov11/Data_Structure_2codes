# Time: O(n), Space: O(1)

class Node:
    def __init__(self, val: int = 0, next_node: "Node | None" = None):
        self.val = val
        self.next = next_node


def has_cycle(head: Node | None) -> bool:
    """Floyd's Cycle Detection Algorithm."""
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def detect_cycle_start(head: Node | None) -> Node | None:
    """Stretch Goal: Returns the exact node where the cycle begins."""
    slow = head
    fast = head
    has_loop = False

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_loop = True
            break

    if not has_loop:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


if __name__ == "__main__":
    # Test Case 1: Cyclic list
    node3 = Node(3)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    node3.next = node2  # Creates cycle: 1 -> 2 -> 3 -> 2
    assert has_cycle(node1) == True
    assert detect_cycle_start(node1) == node2

    # Test Case 2: Acyclic list
    line_head = Node(1, Node(2, Node(3)))
    assert has_cycle(line_head) == False
    assert detect_cycle_start(line_head) is None

    # Test Case 3: Single node self-loop and empty list (edge cases)
    self_loop = Node(1)
    self_loop.next = self_loop
    assert has_cycle(self_loop) == True
    assert has_cycle(None) == False
    print("Challenge 5 tests passed!")
