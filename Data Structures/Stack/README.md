# Stack

## Introduction
The Stack is a fundamental data structure that follows the Last-In, First-Out (LIFO) principle. It is used when you need to manage a collection of elements where the most recently added element is the first one to be removed. Common use cases include function call management, undo mechanisms in applications, and parsing expressions.

## Usage

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())  # Output: 3
print(stack.pop())   # Output: 3
print(stack.size())  # Output: 2
print(stack.is_empty())  # Output: False


## Detailed Explanation
The `Stack` class is implemented using a Python list to store its elements. It provides methods to push items onto the stack, pop items from the top, peek at the top item, check if the stack is empty, and get the size of the stack. The class also includes special methods for string representation and length checking.

## Complexity Analysis
- **Push:** O(1) - Adding an element to the end of a list is constant time.
- **Pop:** O(1) - Removing the last element from a list is constant time.
- **Peek:** O(1) - Accessing the last element of a list is constant time.
- **Is Empty:** O(1) - Checking if the list is empty is constant time.
- **Size:** O(1) - Getting the size of the list is constant time.