class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            new = BinaryTree(value)
            new.left_child = self.left_child
            self.left_child = new

    def insert_right(self, value):
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            new = BinaryTree(value)
            new.right_child = self.right_child
            self.right_child = new

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
