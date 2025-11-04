# MaxHeap Data Structure

## 1. Introduction
A MaxHeap is a specialized binary tree-based data structure that satisfies the max-heap property: every parent node is greater than or equal to its children. This enables efficient retrieval, insertion, and extraction of the maximum element in logarithmic time. It is widely used for priority queue implementations, heap sort algorithms, and scenarios where frequent access to the largest element is required.

## 2. Usage
Create a MaxHeap instance:
heap = MaxHeap()
Insert elements:
heap.insert(10)
heap.insert(5)
heap.insert(20)
Peek at the maximum element:
max_val = heap.peek_max()
print(f"Max element: {max_val}")  # Output: Max element: 20
Extract the maximum element:
extracted = heap.extract_max()
print(f"Extracted max: {extracted}")       # Output: Extracted max: 20
Heapify an existing array:
arr = [3, 9, 2, 1, 4, 5]
heap.heapify(arr)
Extract max after heapify:
print(heap.extract_max())  # Output: 9
Size of the heap:
print(heap.size())  # Output: current number of elements in the heap

## 3. Detailed Explanation
The MaxHeap class maintains the heap in a zero-based indexed array where each node's children are at indices 2*i + 1 and 2*i + 2 and the parent at (i - 1) // 2.

- insert(key): Adds the new key at the end of the list and then moves it upward (_sift_up) until the max-heap property is restored.
- extract_max(): Removes the root element (maximum). Replaces the root with the last element, then moves this element down (_sift_down).
- peek_max(): Returns the root element without modifying it.
- heapify(array): Converts an unsorted list into a valid max-heap by performing _sift_down from the last parent down to the root, in O(n).
- Helper methods _sift_up(idx) and _sift_down(idx) restore the heap property after insertions and deletions.

## 4. Complexity Analysis
- Insertion (insert): O(log n) time.
- Extraction (extract_max): O(log n) time.
- Peek max (peek_max): O(1) time.
- Heap construction (heapify): O(n) time.
- Space complexity: O(n).