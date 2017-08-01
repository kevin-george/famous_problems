"""
The Vertex maintains a list of the ids of the vertexes
that are its neighbors
"""
class Vertex:
    def __init__(self, vertex_id):
        self.__id = vertex_id
        self.__neighbors = {}
        self.__discovered = False
        self.__processed = False

    def get_neighbors(self):
        return self.__neighbors.keys()

    def add_neighbor(self, vertex_id, cost):
        self.__neighbors[vertex_id] = cost

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def get_cost(self, vertex_id):
        return self.__neighbors[vertex_id]

    def set_cost(self, vertex_id, cost):
        if vertex_id in self.__neighbors:
            self.__neighbors[vertex] = cost
        else:
            raise ValueError("{} is not a neighbor".format(vertex_id))

    @property
    def discovered(self):
        return self.__discovered

    @discovered.setter
    def discovered(self, value):
        self.__discovered = value

    @property
    def processed(self):
        return self.__processed

    @processed.setter
    def processed(self, value):
        self.__processed = value

"""
The Graph maintains a list of Vertex instances in it
"""
class Graph:
    def __init__(self):
        self.vertex_list = {}

    def add_vertex(self, vertex_id):
        self.vertex_list[vertex_id] = Vertex(vertex_id)

    def add_edge(self, from_vertex_id, to_vertex_id, cost = 0):
        if from_vertex_id not in self.vertex_list:
            self.add_vertex(from_vertex_id)
        if to_vertex_id not in self.vertex_list:
            self.add_vertex(to_vertex_id)
        self.vertex_list[from_vertex_id].add_neighbor(to_vertex_id, cost)

    def get_vertex(self, vertex_id):
        if vertex_id in self.vertex_list:
            return self.vertex_list[vertex_id]

    def get_vertices(self):
        return self.vertex_list

    def __contains__(self, vertex_id):
        return vertex_id in self.vertex_list

    def reset(self):
        vertices = self.vertex_list.values()
        for vert in vertices:
            vert.processed = False
            vert.discovered = False
