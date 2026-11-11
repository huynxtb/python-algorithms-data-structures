class SelfOrganizingList:
    def __init__(self):
        self.elements = []
        self.element_set = set()

    def insert(self, element):
        if element not in self.element_set:
            self.elements.append(element)
            self.element_set.add(element)

    def access(self, element):
        if element in self.element_set:
            self.elements.remove(element)
            self.elements.insert(0, element)

    def delete(self, element):
        if element in self.element_set:
            self.elements.remove(element)
            self.element_set.remove(element)