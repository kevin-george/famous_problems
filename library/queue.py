class Queue:
    def __init__(self):
        self.elements = []

    def addQueue(self, item):
        self.elements.insert(0, item)

    def removeQueue(self):
        return self.elements.pop()

    def isEmpty(self):
        return len(self.elements) == 0

    def size(self):
        return len(self.elements)

    def peek(self):
        if len(self.elements) > 0:
            return self.elements[len(self.elements) - 1]
