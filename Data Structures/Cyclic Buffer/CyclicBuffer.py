class CyclicBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.count = 0

    def write(self, data):
        self.buffer[self.head] = data
        if self.count < self.size:
            self.count += 1
        self.head = (self.head + 1) % self.size

    def read(self):
        if self.count == 0:
            raise IndexError('Read from empty buffer')
        read_index = (self.head - self.count + self.size) % self.size
        data = self.buffer[read_index]
        self.count -= 1
        return data

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def __str__(self):
        return str([self.buffer[(self.head - i - 1) % self.size] for i in range(self.count)])