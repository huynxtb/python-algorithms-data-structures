# Singly Linked List

## Introduction

A Singly Linked List is a fundamental linear data structure where elements are stored in nodes. Each node contains data and a reference (or pointer) to the next node in the sequence. Unlike arrays, linked lists do not store elements in contiguous memory locations, allowing for dynamic resizing and efficient insertions/deletions, especially at the beginning and end. However, accessing elements by index can be less efficient than in arrays.

**When to use it:**
*   When you need frequent insertions or deletions at the beginning or end of a collection.
*   When the size of the collection is dynamic and unpredictable.
*   When memory is a concern and you want to avoid the overhead of pre-allocating large contiguous blocks of memory.
*   As a building block for other data structures like stacks and queues.

## Usage


# Create a new linked list
my_list = SinglyLinkedList()

# Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
print(f"After appending: {my_list}") # Output: After appending: 10 -> 20 -> 30 -> None

# Prepend elements
my_list.prepend(5)
print(f"After prepending: {my_list}") # Output: After appending: 5 -> 10 -> 20 -> 30 -> None

# Insert after a specific element
my_list.insert_after(20, 25)
print(f"After inserting 25 after 20: {my_list}") # Output: After inserting 25 after 20: 5 -> 10 -> 20 -> 25 -> 30 -> None

# Find an element
found_node = my_list.find(10)
if found_node:
    print(f"Found node with data: {found_node.data}") # Output: Found node with data: 10

# Get element at index
print(f"Element at index 2: {my_list.get_at_index(2)}") # Output: Element at index 2: 20

# Get list length
print(f"List length: {len(my_list)}") # Output: List length: 6

# Iterate through the list
print("Iterating through the list:")
for item in my_list:
    print(item)
# Output:
# 5
# 10
# 20
# 25
# 30

# Delete an element
my_list.delete(20)
print(f"After deleting 20: {my_list}") # Output: After deleting 20: 5 -> 10 -> 25 -> 30 -> None

# Attempt to delete a non-existent element (will raise ValueError)
# try:
#     my_list.delete(100)
# except ValueError as e:
#     print(e)

# Attempt to get out of bounds index (will raise IndexError)
# try:
#     my_list.get_at_index(10)
# except IndexError as e:
#     print(e)


## Detailed Explanation

### `Node` Class

*   **`__init__(self, data, next_node=None)`**: The constructor initializes a node with `data` and an optional `next_node`. `next_node` defaults to `None`, indicating the end of a sequence.
*   **`@property data` / `@data.setter`**: These provide controlled access to the `_data` attribute. You can get the data using `node.data` and set it using `node.data = new_value`.
*   **`@property next_node` / `@next_node.setter`**: Similar to `data`, these manage access to the `_next_node` attribute, allowing you to get or set the reference to the subsequent node.

### `SinglyLinkedList` Class

*   **`__init__(self)`**: Initializes an empty list by setting `self.head` to `None` (no nodes yet) and `self._size` to `0`.
*   **`append(self, data)`**:
    *   Creates a new `Node` with the given `data`.
    *   If the list is empty (`self.head` is `None`), the new node becomes the `head`.
    *   Otherwise, it traverses the list from the `head` until it finds the last node (where `current.next_node` is `None`).
    *   The `next_node` of the last node is then set to the `new_node`.
    *   `self._size` is incremented.
*   **`prepend(self, data)`**:
    *   Creates a new `Node` with the given `data`.
    *   The `next_node` of this new node is set to the current `self.head`.
    *   `self.head` is updated to point to the `new_node`, effectively placing it at the beginning.
    *   `self._size` is incremented.
*   **`insert_after(self, target_data, new_data)`**:
    *   Iterates through the list to find the first node whose `data` matches `target_data`.
    *   If found, a `new_node` is created with `new_data`. Its `next_node` is set to the `target_node`'s original `next_node`.
    *   The `target_node`'s `next_node` is then updated to point to the `new_node`.
    *   `self._size` is incremented.
    *   If `target_data` is not found after traversing the entire list, a `ValueError` is raised.
*   **`delete(self, data)`**:
    *   Handles the case of an empty list.
    *   Checks if the `head` node contains the `data` to be deleted. If so, `self.head` is updated to `self.head.next_node`.
    *   Otherwise, it iterates through the list, keeping track of the `current` node. It checks `current.next_node.data`.
    *   If a match is found, `current.next_node` is updated to skip the node to be deleted (`current.next_node.next_node`).
    *   `self._size` is decremented.
    *   If the `data` is not found, a `ValueError` is raised.
*   **`find(self, data)`**:
    *   Traverses the list from the `head`.
    *   If a node's `data` matches the search `data`, that `Node` object is returned.
    *   If the end of the list is reached without finding the `data`, `None` is returned.
*   **`get_at_index(self, index)`**:
    *   Performs bounds checking to ensure the `index` is valid (non-negative and less than `self._size`). Raises `IndexError` if invalid.
    *   Traverses the list `index` times, moving `current` forward.
    *   Returns the `data` of the node at that position.
*   **`__len__(self)`**: Returns the current count of nodes stored in `self._size`.
*   **`__str__(self)`**:
    *   Constructs a list of string representations of each node's data.
    *   Joins these strings with " -> " and appends " -> None" to represent the end of the list.
*   **`__iter__(self)`**:
    *   Implements the iterator protocol.
    *   It's a generator function that yields the `data` of each node sequentially as it traverses the list.

## Complexity Analysis

Let N be the number of nodes in the linked list.

*   **`append(data)`**:
    *   Time Complexity: O(N) - Requires traversing to the end of the list.
    *   Space Complexity: O(1) - Only a new node is created.
*   **`prepend(data)`**:
    *   Time Complexity: O(1) - Only head manipulation is needed.
    *   Space Complexity: O(1) - Only a new node is created.
*   **`insert_after(target_data, new_data)`**:
    *   Time Complexity: O(N) - In the worst case, `target_data` is the last element or not found, requiring traversal of the entire list.
    *   Space Complexity: O(1) - Only a new node is created.
*   **`delete(data)`**:
    *   Time Complexity: O(N) - In the worst case, the element to be deleted is the last one or not present, requiring traversal.
    *   Space Complexity: O(1) - No significant extra space is used.
*   **`find(data)`**:
    *   Time Complexity: O(N) - In the worst case, the element is at the end or not present.
    *   Space Complexity: O(1) - No significant extra space is used.
*   **`get_at_index(index)`**:
    *   Time Complexity: O(N) - Requires traversing up to the `index`.
    *   Space Complexity: O(1) - No significant extra space is used.
*   **`__len__()`**:
    *   Time Complexity: O(1) - Returns a pre-computed size.
    *   Space Complexity: O(1).
*   **`__str__()`**:
    *   Time Complexity: O(N) - Requires traversing the entire list to build the string.
    *   Space Complexity: O(N) - To store the string representation.
*   **`__iter__()`**:
    *   Time Complexity: O(N) - Each iteration traverses one step.
    *   Space Complexity: O(1) - The iterator itself uses constant space.