# Self-Organizing List

## Introduction
The Self-Organizing List is a data structure designed to optimize access times for frequently accessed elements. It rearranges itself based on access patterns, moving accessed elements to the front of the list, which can significantly improve performance in scenarios with repeated accesses.

## Usage

sol = SelfOrganizingList()
sol.insert(1)
sol.insert(2)
sol.access(1)  # Moves 1 to the front
sol.delete(2)


## Detailed Explanation
The `SelfOrganizingList` class maintains a list of elements and a set for quick lookups. The `insert` method adds elements to the list if they are not already present. The `access` method retrieves an element, moving it to the front of the list if it exists. The `delete` method removes an element from both the list and the set if it exists. This structure allows for efficient management of frequently accessed elements, enhancing performance in specific use cases.

## Complexity Analysis
- **Insert:** O(1) on average, since adding to the end of a list and checking membership in a set are both average O(1) operations.
- **Access:** O(n) in the worst case, as it may require removing an element from the middle of the list and inserting it at the front.
- **Delete:** O(n) in the worst case, as it may require finding and removing an element from the list.