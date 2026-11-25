# Min-Heap

## Introduction
A Min-Heap is a complete binary tree where the value of each node is less than or equal to the values of its children. It is particularly useful for implementing priority queues and algorithms that require frequent access to the minimum value.

## Usage

heap = MinHeap()
heap.insert(10)
heap.insert(5)
heap.insert(20)
print(heap.peek_min())  # Output: 5
print(heap.extract_min())  # Output: 5
print(heap.size())  # Output: 2
print(heap.is_empty())  # Output: False


## Detailed Explanation
The `MinHeap` class maintains a list to store the heap elements. The `insert` method adds a new item and restores the heap property using the `_heapify_up` method. The `extract_min` method removes the smallest item (the root) and restores the heap property using `_heapify_down`. The `peek_min` method allows access to the smallest item without removing it. Helper methods calculate parent and child indices and swap elements as needed.

## Complexity Analysis
- **Insert:** O(log n)  
- **Extract Min:** O(log n)  
- **Peek Min:** O(1)  
- **Is Empty:** O(1)  
- **Size:** O(1)