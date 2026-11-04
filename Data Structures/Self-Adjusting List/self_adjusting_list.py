class SelfAdjustingList:
    def __init__(self):
        self.elements = []

    def access(self, element):
        index = self._find_index(element)
        if index != -1:
            self._move_to_front(index)

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def remove(self, element):
        index = self._find_index(element)
        if index != -1:
            self._remove_at_index(index)

    def _find_index(self, element):
        for i in range(len(self.elements)):
            if self.elements[i] == element:
                return i
        return -1

    def _move_to_front(self, index):
        element = self.elements[index]
        for i in range(index, 0, -1):
            self.elements[i] = self.elements[i - 1]
        self.elements[0] = element

    def _remove_at_index(self, index):
        for i in range(index, len(self.elements) - 1):
            self.elements[i] = self.elements[i + 1]
        self.elements.pop()