class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SelfBalancingCircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        self.size += 1
        self.balance()

    def delete(self, data):
        if self.head is None:
            return
        current = self.head
        prev = None
        while True:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    # Deleting head
                    if current.next == self.head:
                        self.head = None
                    else:
                        last = self.head
                        while last.next != self.head:
                            last = last.next
                        last.next = current.next
                        self.head = current.next
                self.size -= 1
                self.balance()
                return
            prev = current
            current = current.next
            if current == self.head:
                break

    def search(self, data):
        if self.head is None:
            return False
        current = self.head
        while True:
            if current.data == data:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def balance(self):
        if self.size < 2:
            return
        mid_index = self.size // 2
        current = self.head
        for _ in range(mid_index):
            current = current.next
        self.head = current

    def display(self):
        if self.head is None:
            return []
        elements = []
        current = self.head
        while True:
            elements.append(current.data)
            current = current.next
            if current == self.head:
                break
        return elements
