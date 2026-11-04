# Self-Adjusting List

## Introduction
The Self-Adjusting List is a data structure designed to optimize access times for frequently accessed elements. By moving accessed elements closer to the front of the list, it improves the efficiency of future access operations. This structure is particularly useful in scenarios where certain elements are accessed more frequently than others, allowing for quicker retrieval.

## Usage

sal = SelfAdjustingList()
sal.add(1)
sal.add(2)
sal.add(3)
sal.access(2)  # Moves 2 to the front
sal.remove(1)  # Removes 1 from the list


## Detailed Explanation
The `SelfAdjustingList` class maintains a list of elements. It provides three main operations: `access`, `add`, and `remove`. The `access` method checks if an element exists and moves it to the front if it does. The `add` method appends a new element to the end of the list if it is not already present. The `remove` method deletes an element from the list if it exists. The internal methods `_find_index`, `_move_to_front`, and `_remove_at_index` are used for managing the list without relying on built-in list methods.

## Complexity Analysis
- **Access:** O(n) - In the worst case, we may need to traverse the entire list to find the element and then move it to the front.
- **Add:** O(n) - We check for existence before adding, which may require traversing the list.
- **Remove:** O(n) - Similar to access, we need to find the element and then remove it, which involves shifting elements.