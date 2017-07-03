from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        n = Node(item)
        n.setNext(self.head)
        self.head = n

    def remove(self, item):
        pointer = self.head
        prev_pointer = None
        while pointer is not None:
            if pointer.getData() == item:
                if prev_pointer is not None:
                    prev_pointer.setNext(pointer.getNext())
                    print("Removed %d" %(item))
                    return
                else:
                    self.head = pointer.getNext()
                    print("Removed %d from head" %(item))
                    return
            prev_pointer = pointer
            pointer = pointer.getNext()
        print("Couldn't find %d" %(item))

    def search(self, item):
        pointer = self.head
        while pointer is not None:
            if pointer.getData() == item:
                return True
            pointer = pointer.getNext()
        return False

    def size(self):
        counter = 0
        pointer = self.head
        while pointer is not None:
            counter += 1
            pointer = pointer.getNext()
        return counter

    def isEmpty(self):
        return self.head is None
