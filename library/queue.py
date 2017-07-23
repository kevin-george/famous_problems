class Queue:
    def __init__(self):
        self.elements = []

    def enqueue(self, item):
        self.elements.insert(0, item)

    def dequeue(self):
        return self.elements.pop()

    def is_empty(self):
        return len(self.elements) == 0

    def size(self):
        return len(self.elements)

    def peek(self):
        if len(self.elements) > 0:
            return self.elements[len(self.elements) - 1]
