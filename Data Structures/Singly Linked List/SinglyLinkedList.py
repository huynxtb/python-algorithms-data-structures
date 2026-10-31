class Node:
    """Represents a single node in a singly linked list."""
    def __init__(self, data, next_node=None):
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        """Gets the data stored in the node."""
        return self._data

    @data.setter
    def data(self, value):
        """Sets the data stored in the node."""
        self._data = value

    @property
    def next_node(self):
        """Gets the next node in the list."""
        return self._next_node

    @next_node.setter
    def next_node(self, node):
        """Sets the next node in the list."""
        self._next_node = node

class SinglyLinkedList:
    """Implements a singly linked list data structure."""
    def __init__(self):
        """Initializes an empty singly linked list."""
        self.head = None
        self._size = 0

    def append(self, data):
        """Adds a new node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
        self._size += 1

    def prepend(self, data):
        """Adds a new node with the given data to the beginning of the list."""
        new_node = Node(data, self.head)
        self.head = new_node
        self._size += 1

    def insert_after(self, target_data, new_data):
        """Inserts a new node with new_data after the first occurrence of target_data."""
        current = self.head
        while current:
            if current.data == target_data:
                new_node = Node(new_data, current.next_node)
                current.next_node = new_node
                self._size += 1
                return
            current = current.next_node
        raise ValueError(f"Target data '{target_data}' not found in the list.")

    def delete(self, data):
        """Removes the first occurrence of a node with the given data."""
        if not self.head:
            raise ValueError(f"Data '{data}' not found in the empty list.")

        if self.head.data == data:
            self.head = self.head.next_node
            self._size -= 1
            return

        current = self.head
        while current.next_node:
            if current.next_node.data == data:
                current.next_node = current.next_node.next_node
                self._size -= 1
                return
            current = current.next_node
        raise ValueError(f"Data '{data}' not found in the list.")

    def find(self, data):
        """Searches for a node with the given data and returns the Node object if found, otherwise None."""
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next_node
        return None

    def get_at_index(self, index):
        """Returns the data of the node at the specified index."""
        if not (0 <= index < self._size):
            raise IndexError(f"Index {index} is out of bounds for list of size {self._size}.")

        current = self.head
        for _ in range(index):
            current = current.next_node
        return current.data

    def __len__(self):
        """Returns the number of nodes in the list."""
        return self._size

    def __str__(self):
        """Returns a string representation of the linked list."""
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return " -> ".join(nodes) + " -> None"

    def __iter__(self):
        """Returns an iterator for the linked list, yielding node data."""
        current = self.head
        while current:
            yield current.data
            current = current.next_node
