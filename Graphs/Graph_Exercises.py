# Graphs are groups of Vertices(nodes) connected by Edges(connections)

# Weighted edges can exist in graphs. Weighted edges are analagous to different
# routes in Google Maps. Route B might be faster than Route A even though the
# total distance in Route B is greater. In this scenario, Route A has a
# "heavier" weight.

# Edges are either directional or bi-directional

# Graphs can be visualized as either an "Adjacency Matrix" or an "Adjacency
# List"

# Graph: Add Vertex

class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

my_graph = Graph()

my_graph.add_vertex('A')

my_graph.print_graph()

# Graph: Add Edge

def add_edge(self, v1, v2):
    if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)
        return True
    return False

my_graph = Graph()

my_graph.add_vertex(1)
my_graph.add_vertex(2)

my_graph.add_edge(1,2)

my_graph.print_graph()

# Graph: Remove Edge

def remove_edge(self, v1, v2):
    if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
        try:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
        except ValueError:
            pass
        return True
    return False

my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A','B')
my_graph.add_edge('B','C')
my_graph.add_edge('C','A')

my_graph.remove_edge('A','D')

my_graph.print_graph()

# Graph: Remove Vertex

def remove_vertex(self, vertex):
    if vertex in self.adj_list.keys():
        for other_vertex in self.adj_list[vertex]:
            self.adj_list[other_vertex].remove(vertex)
        del self.adj_list[vertex]
        return True
    return False

my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A','B')
my_graph.add_edge('A','C')
my_graph.add_edge('A','D')
my_graph.add_edge('B','D')
my_graph.add_edge('C','D')

my_graph.remove_vertex('D')

my_graph.print_graph()

