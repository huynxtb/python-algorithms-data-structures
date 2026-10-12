class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal_iterative(root: TreeNode) -> list[int]:
    """
    Performs an inorder traversal of a binary tree iteratively using a stack.

    Inorder traversal visits nodes in the order: Left -> Root -> Right.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of integers representing the values of the nodes in inorder.
    """
    result = []
    stack = []
    current_node = root

    while current_node is not None or stack:
        # Traverse to the leftmost node, pushing all visited nodes onto the stack
        while current_node is not None:
            stack.append(current_node)
            current_node = current_node.left

        # current_node is None, meaning we've reached the end of a left path
        # Pop the last node from the stack, which is the current root to visit
        current_node = stack.pop()
        result.append(current_node.val)

        # Now, move to the right child to process its subtree
        current_node = current_node.right

    return result
