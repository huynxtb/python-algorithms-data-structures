# Self-Balancing Circular Linked List

## Introduction
The Self-Balancing Circular Linked List is a data structure that combines the properties of a circular linked list with self-balancing capabilities. This structure is useful when you need a circular list that maintains an even distribution of nodes, ensuring efficient access and modification.

## Usage

scll = SelfBalancingCircularLinkedList()
scll.insert(10)
scll.insert(20)
scll.insert(30)
scll.delete(20)
print(scll.display())  # Output: [30, 10]
print(scll.search(10))  # Output: True
print(scll.search(20))  # Output: False


## Detailed Explanation
The Self-Balancing Circular Linked List consists of nodes that point to the next node in a circular manner. The `insert` method adds a new node to the list and calls the `balance` method to ensure the list remains balanced after insertion. The `delete` method removes a node and also balances the list afterward. The `search` method checks for the existence of a node in the list. The `balance` method adjusts the head of the list to maintain an even distribution of nodes around it.

## Complexity Analysis
- **Insertion:** O(1) for adding a node, O(n) for balancing (in the worst case), so overall O(n).
- **Deletion:** O(n) for searching the node, O(n) for balancing, so overall O(n).
- **Search:** O(n) as it may need to traverse the entire list.
- **Space Complexity:** O(n) for storing the nodes in the list.