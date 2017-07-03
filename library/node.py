class Node:
    def __init__(self, init):
        self.data = init
        self.next = None

    def __str__(self):
        if self.next == None:
            return "Data: " + str(self.data) + " Next: " + str(self.next)
        else:
            return "Data: " + str(self.data) + " Next: " + str(self.next.getData())

    def getData(self):
        return self.data

    def setData(self, item):
        self.data = item

    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node
