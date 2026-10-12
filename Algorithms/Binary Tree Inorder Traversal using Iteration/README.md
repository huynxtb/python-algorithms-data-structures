# Binary Tree Inorder Traversal using Iteration

## 1. Introduction
Inorder traversal is a type of depth-first traversal for binary trees. It visits nodes in the order: Left subtree -> Root node -> Right subtree. This means that for a Binary Search Tree (BST), an inorder traversal will visit the nodes in ascending order of their values.

While inorder traversal is often implemented recursively due to its natural fit with the recursive definition of a tree, an iterative approach using a stack can be beneficial. It avoids the potential for stack overflow errors in very deep trees (which can occur with recursion) and can sometimes offer better performance or more explicit control over the traversal process. This implementation provides an iterative solution to perform inorder traversal.

## 2. Usage
To use this algorithm, you first need to define your binary tree using the `TreeNode` class. Then, pass the root of your tree to the `inorder_traversal_iterative` function.


# Define the TreeNode class (included in the solution)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example Usage:
# Construct a sample binary tree:
#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Perform inorder traversal
result = inorder_traversal_iterative(root)
print(f"Inorder traversal: {result}") # Expected output: [4, 2, 5, 1, 3]

# Another example:
#        10
#       /  \
#      5    15
#     / \    /
#    3   7  12
root2 = TreeNode(10)
root2.left = TreeNode(5)
root2.right = TreeNode(15)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(7)
root2.right.left = TreeNode(12)

result2 = inorder_traversal_iterative(root2)
print(f"Inorder traversal: {result2}") # Expected output: [3, 5, 7, 10, 12, 15]


## 3. Detailed Explanation
The iterative inorder traversal algorithm simulates the call stack of a recursive traversal using an explicit stack data structure.

1.  **Initialization**:
    *   `result`: An empty list to store the values of nodes in inorder.
    *   `stack`: An empty list used as a stack to keep track of nodes whose left subtrees have been processed but the node itself and its right subtree still need to be visited.
    *   `current_node`: A pointer initialized to the `root` of the tree. This pointer helps us traverse down the tree.

2.  **Main Loop**: The algorithm continues as long as `current_node` is not `None` (meaning there are still nodes to potentially visit) or the `stack` is not empty (meaning there are parent nodes whose right subtrees haven't been processed yet).

3.  **Traversing Left Subtree**:
    *   The inner `while current_node is not None` loop is responsible for traversing as far left as possible from the `current_node`.
    *   As it moves left, each `current_node` encountered is pushed onto the `stack`. This is crucial because these nodes are "roots" that need to be visited *after* their left children but *before* their right children.
    *   `current_node` is updated to `current_node.left` in each step.

4.  **Visiting the Node (Root)**:
    *   Once the inner loop finishes, `current_node` will be `None`. This signifies that we've reached the end of a left path (either an actual `None` child or the leftmost node of a subtree).
    *   At this point, the topmost node on the `stack` is the one whose left subtree (or lack thereof) has been fully explored. This node is the "root" that should be visited next in inorder traversal.
    *   We `pop` this node from the `stack`, assign it back to `current_node`, and add its `val` to our `result` list.

5.  **Traversing Right Subtree**:
    *   After visiting the `current_node` (which was just popped), we need to process its right subtree.
    *   We update `current_node` to `current_node.right`. The main `while` loop will then restart, and if `current_node` is not `None`, it will again try to go as far left as possible from this new `current_node` (the right child). If `current_node` is `None`, the loop will continue by popping the next node from the stack.

This process ensures that nodes are visited in the correct Left -> Root -> Right order without explicit recursion.

## 4. Complexity Analysis

*   **Time Complexity**: O(N)
    *   Each node in the binary tree is visited and processed (pushed onto the stack and popped from the stack) exactly once. Therefore, the time complexity is directly proportional to the number of nodes (N) in the tree.

*   **Space Complexity**: O(H)
    *   The space complexity is determined by the maximum size of the `stack`. In the worst-case scenario, if the tree is completely skewed (e.g., a linked list where every node only has a left child), the stack might hold all N nodes. In this case, H = N, and the space complexity is O(N).
    *   In the best-case scenario (a perfectly balanced binary tree), the height H is approximately log N. Thus, the stack would hold at most O(log N) nodes.
    *   Therefore, the space complexity is O(H), where H is the height of the binary tree.
