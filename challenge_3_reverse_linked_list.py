# Time: O(n), Space: O(1) Iterative / O(n) Recursive

class Node:
    def __init__(self, val: int = 0, next_node: "Node | None" = None):
        self.val = val
        self.next = next_node


def reverse_list(head: Node | None) -> Node | None:
    """Iterative reversal of singly linked list in O(1) space."""
    prev = None
    curr = head
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def reverse_list_recursive(head: Node | None) -> Node | None:
    """Stretch Goal: Recursive reversal.
    
    Note on Space Complexity:
    This recursive implementation requires O(n) space because each recursive call
    adds a frame to the call stack until reaching the tail node.
    """
    if head is None or head.next is None:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


# Helper for testing
def to_list(head: Node | None) -> list[int]:
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res


if __name__ == "__main__":
    # Test Case 1: Multi-node list
    head1 = Node(1, Node(2, Node(3)))
    assert to_list(reverse_list(head1)) == [3, 2, 1]

    # Test Case 2: Single-node list
    head2 = Node(1)
    assert to_list(reverse_list(head2)) == [1]

    # Test Case 3: Empty list (edge case) & Recursive stretch test
    assert reverse_list(None) is None
    head3 = Node(1, Node(2, Node(3)))
    assert to_list(reverse_list_recursive(head3)) == [3, 2, 1]
    print("Challenge 3 tests passed!")
