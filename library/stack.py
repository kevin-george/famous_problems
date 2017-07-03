class Stack:
    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        return self.elements.pop()

    def peek(self):
        if len(self.elements) > 0:
            return self.elements[-1]

    def isEmpty(self):
        return len(self.elements) == 0

    def size(self):
        return len(self.elements)
