# Time: O(n), Space: O(h) recursion stack / explicit stack

class Node:
    def __init__(self, val: int = 0, left: "Node | None" = None, right: "Node | None" = None):
        self.val = val
        self.left = left
        self.right = right


# Note: We assume strictly increasing BST values (left < node < right).
def is_valid_bst(root: Node | None, low: float = float("-inf"), high: float = float("inf")) -> bool:
    """Recursive BST Validation with bounded range propagation."""
    if root is None:
        return True
    if not (low < root.val < high):
        return False
    return is_valid_bst(root.left, low, root.val) and is_valid_bst(root.right, root.val, high)


def is_valid_bst_iterative(root: Node | None) -> bool:
    """Stretch Goal: Iterative BST validation using an explicit stack."""
    if root is None:
        return True
    stack = [(root, float("-inf"), float("inf"))]
    while stack:
        node, low, high = stack.pop()
        if not (low < node.val < high):
            return False
        if node.right:
            stack.append((node.right, node.val, high))
        if node.left:
            stack.append((node.left, low, node.val))
    return True


if __name__ == "__main__":
    # Test Case 1: Valid BST
    valid_root = Node(2, Node(1), Node(3))
    assert is_valid_bst(valid_root) == True
    assert is_valid_bst_iterative(valid_root) == True

    # Test Case 2: Invalid BST (sub-child violates ancestor bound)
    # Tree: 5 / \ 1 8 (left child 4 violates 5 < 8)
    invalid_root = Node(5, Node(1), Node(8, Node(4), Node(9)))
    assert is_valid_bst(invalid_root) == False
    assert is_valid_bst_iterative(invalid_root) == False

    # Test Case 3: Empty tree & single node (edge cases)
    assert is_valid_bst(None) == True
    assert is_valid_bst(Node(42)) == True
    print("Challenge 8 tests passed!")
