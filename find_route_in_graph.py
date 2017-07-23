from library.graphs import Graph
from library.graphs import Vertex
from library.queue import Queue
from nose.tools import assert_equal

"""
Using breadth first search, assuming branching factor for
graph is low so space complexity is not an issue
"""
def does_route_exist(g, from_vert_id, to_vert_id):
    q = Queue()
    q.enqueue(from_vert_id)
    while not(q.is_empty()):
        vert_id = q.dequeue()
        vert = g.get_vertex(vert_id)
        if not(vert.visited):
            nbrs = vert.get_neighbors()
            for nbr in nbrs:
                if nbr == to_vert_id:
                    return True
                q.enqueue(nbr)
        vert.visited = True
    return False

g = Graph()
g.add_edge('b', 'a')
g.add_edge('b', 'c')
g.add_edge('c', 'b')
g.add_edge('c', 'd')
g.add_edge('c', 'e')

assert_equal(does_route_exist(g, 'a', 'e'), False)
assert_equal(does_route_exist(g, 'c', 'd'), True)
assert_equal(does_route_exist(g, 'd', 'e'), False)
assert_equal(does_route_exist(g, 'a', 'b'), False)
assert_equal(does_route_exist(g, 'b', 'e'), True)
