from library.binary_tree import BinaryTree
from nose.tools import assert_equal

"""
Parser to check for perfectly balanced Binary Trees
"""

def parse_tree(node):
    if node is not None:
        parse_tree(node.left_child)
        parse_tree(node.right_child)
    else:
        return
    if node.left_child is not None:
        node.height = node.left_child.height + 1
    elif node.right_child is not None:
        node.height = node.right_child.height + 1
    else:
        node.height = 0

def check_if_balanced(node):
    parse_tree(node)
    if node:
        lh = node.left_child.height if node.left_child else 0
        rh = node.right_child.height if node.right_child else 0
        bf = lh - rh
        return True if bf == 0 else False
    else:
        return True

# Tree depiction
#        a
#    b       c
#d      e f     g
a = BinaryTree('a')
a.left_child = 'b'
a.right_child = 'c'
b = a.left_child
b.left_child = 'd'
b.right_child = 'e'
c = a.right_child
c.left_child = 'f'
c.right_child = 'g'
assert_equal(check_if_balanced(a), True)

# Tree depiction
#        a
#    b
#d      e
a = BinaryTree('a')
a.left_child = 'b'
b = a.left_child
b.left_child = 'd'
b.right_child = 'e'
assert_equal(check_if_balanced(a), False)

# Tree depiction
#        a
a = BinaryTree('a')
assert_equal(check_if_balanced(a), True)

# Tree depiction
assert_equal(check_if_balanced(None), True)
