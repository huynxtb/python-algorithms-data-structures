class Stack:
    """
    A Stack data structure that follows Last-In, First-Out (LIFO) principle.
    """

    def __init__(self) -> None:
        """
        Initializes an empty stack.
        """
        self._elements = []

    def push(self, item) -> None:
        """
        Adds the given item to the top of the stack.
        
        :param item: The item to be added to the stack.
        """
        self._elements.append(item)

    def pop(self):
        """
        Removes and returns the item from the top of the stack.
        Raises IndexError if the stack is empty.
        
        :return: The item from the top of the stack.
        :raises IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._elements.pop()

    def peek(self):
        """
        Returns the item from the top of the stack without removing it.
        Raises IndexError if the stack is empty.
        
        :return: The item from the top of the stack.
        :raises IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._elements[-1]

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.
        
        :return: True if the stack is empty, False otherwise.
        """
        return len(self._elements) == 0

    def size(self) -> int:
        """
        Returns the number of elements currently in the stack.
        
        :return: The size of the stack.
        """
        return len(self._elements)

    def __len__(self) -> int:
        """
        Allows the built-in len() function to return the size of the stack.
        
        :return: The size of the stack.
        """
        return self.size()

    def __str__(self) -> str:
        """
        Provides a user-friendly string representation of the stack.
        
        :return: A string representation of the stack.
        """
        return str(self._elements)

    def __repr__(self) -> str:
        """
        Provides an unambiguous string representation of the stack.
        
        :return: A string that could be used to recreate the stack.
        """
        return f"Stack({self._elements})"