# Introduction
A Doubly Linked List is a data structure that consists of nodes, where each node contains a value and two pointers: one pointing to the next node and another pointing to the previous node. This structure allows for efficient insertion, deletion, and traversal of elements in both directions. It is particularly useful when you need to frequently add or remove elements from both ends of the list or when bidirectional traversal is required.

# Usage

# Create a new Doubly Linked List
dll = DoublyLinkedList()

# Append values
 dll.append(1)
dll.append(2)
dll.append(3)

# Prepend values
dll.prepend(0)

# Delete a value
dll.delete(2)

# Find a value
node = dll.find(1)

# Traverse forward
forward_values = dll.traverse_forward()

# Traverse backward
backward_values = dll.traverse_backward()


# Detailed Explanation
The `Node` class represents each element in the doubly linked list, containing a value and pointers to the next and previous nodes. The `DoublyLinkedList` class manages the list, providing methods to append, prepend, delete, find, and traverse the nodes. The `append` method adds a node to the end, while `prepend` adds to the beginning. The `delete` method removes a node by value, and `find` retrieves a node. The traversal methods return lists of values in forward and backward directions, respectively.

# Complexity Analysis
- **Append:** O(1) - Adding to the end is constant time if the tail is maintained.
- **Prepend:** O(1) - Adding to the beginning is also constant time.
- **Delete:** O(n) - In the worst case, we may need to traverse the entire list to find the node.
- **Find:** O(n) - Similar to deletion, finding a node requires traversal.
- **Traverse Forward/Backward:** O(n) - Both operations require visiting each node once.