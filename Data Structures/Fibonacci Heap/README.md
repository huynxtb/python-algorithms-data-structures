# Fibonacci Heap

## 1. Introduction

A Fibonacci Heap is a sophisticated data structure for priority queue operations, offering very efficient amortized running times for common operations such as insertions, minimum extraction, and key decreases. It is particularly advantageous in graph algorithms like Dijkstra's shortest path and Prim's minimum spanning tree where the decrease-key operation is common.

A Fibonacci Heap is a collection of heap-ordered trees, which are structured in a way that supports quick access to the minimum element and allows efficient merging of heaps.

## 2. Usage

Below is an example illustrating the basic usage of the Fibonacci Heap class in Python:

# Create a new Fibonacci Heap
fib_heap = FibonacciHeap()

# Insert some keys
node1 = fib_heap.insert(10)
node2 = fib_heap.insert(3)
node3 = fib_heap.insert(15)

# Find the minimum key
min_key = fib_heap.find_min()  # Expected 3

# Extract the minimum
extracted_min = fib_heap.extract_min()  # Expected 3

# Decrease key of a node
fib_heap.decrease_key(node3, 5)  # Decrease key from 15 to 5

# Delete a node
fib_heap.delete(node1)  # Deletes node with key 10

# Union with another Fibonacci heap
other_heap = FibonacciHeap()
other_heap.insert(2)
fib_heap.union(other_heap)

# Find new minimum
new_min = fib_heap.find_min()  # Expected 2

## 3. Detailed Explanation

- Node Structure: Each node contains its key value, pointers to its parent and child, pointers to its left and right siblings, its degree (number of children), and a mark bit used in cascading cuts.

- Insertion: Insertions add a new node directly to the root list and update the minimum pointer if necessary.

- Find Minimum: Returns the minimum key stored, tracked explicitly.

- Extract Minimum: Removes the minimum node, promotes its children to the root list, and then consolidates the heap by linking trees of the same degree to maintain a balanced structure.

- Decrease Key: Decreases a node's key and cuts it from its parent if the heap ordering is violated, performing cascading cuts to maintain heap properties.

- Delete: Achieved by decreasing the key to negative infinity and then extracting the minimum.

- Union: Merges two heaps by concatenating their root lists and updating the minimum pointer.

Internal helper methods manage list concatenations, node linking, cutting, and cascading cuts.

## 4. Complexity Analysis

| Operation       | Amortized Time Complexity | Description                    |
|-----------------|----------------------------|--------------------------------|
| Insert          | O(1)                       | Adds a node to the root list.  |
| Find Minimum    | O(1)                       | Directly returns the min node. |
| Extract Minimum | O(log n)                   | Removes min and consolidates heap. |
| Decrease Key    | O(1)                       | Cuts and cascades if needed.   |
| Delete          | O(log n)                   | Combination of decrease_key and extract_min. |
| Union           | O(1)                       | Concatenates root lists. |

Space complexity: O(n), where n is the number of nodes stored. Each node maintains pointers and auxiliary information.

This implementation is suitable for integration into larger projects that need an efficient priority queue with advanced operations.