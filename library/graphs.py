class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.neighbors = {}

    def add_neighbor(self, vertex, cost):
        self.neighbors[vertex] = cost

    def get_neighbors(self):
        return self.neighbors.keys()

    def get_id(self):
        return self.id

    def get_cost(self, vertex):
        return self.neighbors[vertex]

    def __str__(self):
        return "Vertex " + self.id + " connected to " + " ".join([x.id for x in self.neighbors])

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
        self.vertex_list[from_vertex_id].add_neighbor(self.vertex_list[to_vertex_id], cost)

    def get_vertices(self):
        return self.vertex_list

    def __contains__(self, vertex_id):
        return vertex_id in self.vertex_list
