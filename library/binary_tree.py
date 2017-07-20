class BinaryTree:
    def __init__(self, value):
        self.__value = value
        self.__left_child = None
        self.__right_child = None
        self.__height = None

    @property
    def left_child(self):
        return self.__left_child

    @left_child.setter
    def left_child(self, value):
        if self.__left_child is None:
            self.__left_child = BinaryTree(value)
        else:
            new = BinaryTree(value)
            new.left_child = self.__left_child
            self.__left_child = new

    @property
    def right_child(self):
        return self.__right_child

    @right_child.setter
    def right_child(self, value):
        if self.__right_child is None:
            self.__right_child = BinaryTree(value)
        else:
            new = BinaryTree(value)
            new.right_child = self.__right_child
            self.__right_child = new

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
