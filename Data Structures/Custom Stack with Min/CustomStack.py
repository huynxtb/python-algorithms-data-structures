class CustomStack:
    """
    A stack data structure that supports standard stack operations (push, pop, peek)
    and also provides a method to retrieve the minimum element in constant time.
    """

    def __init__(self):
        """
        Initializes an empty CustomStack.
        _stack stores the actual elements.
        _min_stack stores the minimum elements encountered so far,
        such that its top always represents the current minimum of _stack.
        """
        self._stack = []
        self._min_stack = []

    def push(self, value):
        """
        Adds an element 'value' to the top of the stack.
        Updates the minimum tracking stack accordingly.

        Args:
            value: The element to be added to the stack.
        """
        self._stack.append(value)
        # If _min_stack is empty or the new value is less than or equal to
        # the current minimum, push it onto _min_stack.
        # Use <= to handle cases where duplicate minimums are pushed.
        # This ensures that when a minimum is popped, its duplicate (if any)
        # remains on _min_stack if it's still the minimum.
        if not self._min_stack or value <= self._min_stack[-1]:
            self._min_stack.append(value)

    def pop(self):
        """
        Removes and returns the top element of the stack.
        If the stack is empty, raises an IndexError.
        Updates the minimum tracking stack if the popped element was the minimum.

        Returns:
            The element removed from the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self._stack:
            raise IndexError("pop from empty stack")

        popped_value = self._stack.pop()
        # If the popped element was the current minimum, remove it from _min_stack as well.
        if popped_value == self._min_stack[-1]:
            self._min_stack.pop()
        return popped_value

    def peek(self):
        """
        Returns the top element of the stack without removing it.
        If the stack is empty, raises an IndexError.

        Returns:
            The top element of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self._stack:
            raise IndexError("peek from empty stack")
        return self._stack[-1]

    def get_min(self):
        """
        Returns the minimum element currently in the stack in constant time.
        If the stack is empty, raises an IndexError.

        Returns:
            The minimum element in the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self._min_stack: # _min_stack is empty if and only if _stack is empty
            raise IndexError("get_min from empty stack")
        return self._min_stack[-1]

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self._stack) == 0

    def size(self):
        """
        Returns the number of elements in the stack.

        Returns:
            int: The number of elements in the stack.
        """
        return len(self._stack)
