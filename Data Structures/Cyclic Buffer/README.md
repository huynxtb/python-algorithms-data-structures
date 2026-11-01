# Cyclic Buffer

## Introduction
The Cyclic Buffer, also known as a circular buffer, is a fixed-size data structure that uses a single, fixed-size buffer as if it were connected end-to-end. It is particularly useful for applications that require a continuous stream of data, such as audio or video processing, where old data can be overwritten by new data when the buffer is full.

## Usage

buffer = CyclicBuffer(3)  # Create a cyclic buffer of size 3
buffer.write(1)           # Write data to the buffer
buffer.write(2)
buffer.write(3)
print(buffer.read())      # Read data from the buffer (outputs 1)
buffer.write(4)           # This will overwrite the oldest data (1)
print(buffer.read())      # Outputs 2
print(buffer.read())      # Outputs 3
print(buffer.read())      # Outputs 4


## Detailed Explanation
The `CyclicBuffer` class maintains an internal list to store the data and uses two pointers: `head` to track where to write the next data and `count` to keep track of the number of elements in the buffer. When writing data, if the buffer is full, the oldest data is overwritten. The `read` method retrieves the next piece of data in the order it was written, and if the buffer is empty, it raises an `IndexError`.

## Complexity Analysis
- **Time Complexity:**
  - `write(data)`: O(1) - Writing data is done in constant time.
  - `read()`: O(1) - Reading data is also done in constant time.
- **Space Complexity:** O(n) - The space complexity is linear with respect to the size of the buffer, where n is the size of the buffer.