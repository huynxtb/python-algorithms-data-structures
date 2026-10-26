## Custom Stack with Min

### 1. Introduction
The `CustomStack` is an enhanced stack data structure that, in addition to standard stack operations like `push`, `pop`, and `peek`, provides the ability to retrieve the minimum element currently in the stack in constant time (O(1)). This is particularly useful in scenarios where efficient access to the minimum value is frequently required without iterating through the entire stack.

### 2. Usage


# Create a new CustomStack
my_stack = CustomStack()

# Push elements onto the stack
my_stack.push(5)
print(f"Pushed 5. Stack: {my_stack._stack}, Min: {my_stack.get_min()}") # Expected Min: 5

my_stack.push(2)
print(f"Pushed 2. Stack: {my_stack._stack}, Min: {my_stack.get_min()}") # Expected Min: 2

my_stack.push(7)
print(f"Pushed 7. Stack: {my_stack._stack}, Min: {my_stack.get_min()}") # Expected Min: 2

my_stack.push(1)
print(f"Pushed 1. Stack: {my_stack._stack}, Min: {my_stack.get_min()}") # Expected Min: 1

# Peek at the top element
print(f"Top element (peek): {my_stack.peek()}") # Expected: 1

# Get the current minimum
print(f"Current minimum: {my_stack.get_min()}") # Expected: 1

# Pop elements
popped_val = my_stack.pop()
print(f"Popped {popped_val}. Stack: {my_stack._stack}, Min: {my_stack.get_min()}") # Expected Popped: 1, Min: 2

popped_val = my_stack.pop()
print(f"Popped {popped_val}. Stack: {my_stack._stack}, Min: {my_stack.get_min()}") # Expected Popped: 7, Min: 2

popped_val = my_stack.pop()
print(f"Popped {popped_val}. Stack: {my_stack._stack}, Min: {my_stack.get_min()}") # Expected Popped: 2, Min: 5

# Check if empty
print(f"Is stack empty? {my_stack.is_empty()}") # Expected: False

# Pop last element
popped_val = my_stack.pop()
print(f"Popped {popped_val}. Stack: {my_stack._stack}, Min: N/A (stack empty after pop)") # Expected Popped: 5

# Try to get min from empty stack (will raise IndexError)
try:
    my_stack.get_min()
except IndexError as e:
    print(f"Error: {e}") # Expected: get_min from empty stack


### 3. Detailed Explanation
The `CustomStack` implementation uses two internal Python lists:
- `_stack`: This list stores all the elements in the standard Last-In, First-Out (LIFO) order, just like a regular stack.
- `_min_stack`: This is an auxiliary stack used to keep track of the minimum elements. The key idea is that `_min_stack` only stores elements that are potential minimums.

Here's how the operations work:
- **`__init__`**: Initializes both `_stack` and `_min_stack` as empty lists.
- **`push(value)`**:
    1. The `value` is always appended to `_stack`.
    2. Before appending to `_min_stack`, it checks two conditions:
        - If `_min_stack` is empty, the `value` is the first element, so it must be the minimum.
        - If `value` is less than or equal to the current top of `_min_stack` (`_min_stack[-1]`), it means `value` is a new minimum (or a duplicate of the current minimum). In this case, `value` is also appended to `_min_stack`. Using `<=` is important to correctly handle scenarios where multiple instances of the same minimum value are pushed and subsequently popped.
- **`pop()`**:
    1. It first checks if `_stack` is empty. If so, it raises an `IndexError`.
    2. The top element is popped from `_stack`.
    3. It then compares the `popped_value` with the top of `_min_stack`. If they are equal, it means the element being removed was the current minimum, so it must also be popped from `_min_stack` to reveal the *previous* minimum.
- **`peek()`**: Returns the top element of `_stack` without removing it, after checking for an empty stack.
- **`get_min()`**: Returns the top element of `_min_stack`. Since `_min_stack` is carefully maintained to always have the current minimum at its top, this operation is O(1). It also checks for an empty stack.
- **`is_empty()` and `size()`**: Standard utility methods for checking stack status.

### 4. Complexity Analysis
- **Time Complexity:**
    - `push(value)`: O(1) - Appending to Python lists is amortized O(1).
    - `pop()`: O(1) - Popping from Python lists is O(1).
    - `peek()`: O(1) - Accessing the last element of a list is O(1).
    - `get_min()`: O(1) - Accessing the last element of a list is O(1).
- **Space Complexity:**
    - O(N) - In the worst case, if elements are pushed in strictly decreasing order, `_min_stack` will store all N elements, similar to `_stack`. Therefore, the total space used is proportional to the number of elements in the stack.