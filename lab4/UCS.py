# coding: utf-8
import queue

def build_path(search_tree, v):
    """ Builds a path in a tree given the target node."""
    if search_tree == None or search_tree == {}:
        return []

    path = []
    while search_tree.has_key(v) and v != None:
        path.insert(0, v)
        v = search_tree[v]
    return path

class Graph(object):
    """
        This implementation actualy doesn't permits:
            - two or more edges between vertices;
    """
    def __init__(self):
        self.edges = {}
        self.distances = {}

    def add_vertice(self, v):
        if v not in self.edges:
            self.edges[v] = []

    def add_edge(self, v1, v2, d=1):
        self.add_vertice(v1)
        self.add_vertice(v2)
        self.edges[v1].append(v2)
        self.distances[(v1, v2)] = d

    def adj(self, v):
        if v not in self.edges:
            raise VerticeNotFoundException
        return self.edges[v]

    def distance(self, v1, v2):
        if (v1, v2) not in self.distances:
            raise EdgeNotFoundException
        return self.distances[(v1, v2)]


class VerticeNotFoundException(BaseException):
    pass


class EdgeNotFoundException(BaseException):
    pass


def ucs(source, target, graph):
    """ Uniform-cost graph search """
    queue = queue.PriorityQueue() # fringe
    queue.put((0, source))

    parent = {source:None}
    visited = {}

    while not queue.empty():
        (d, v_in) = queue.get()

        if v_in not in visited or d < visited[v_in]:

            if v_in == target:
                return (d, build_path(parent, target))

            for v_out in graph.adj(v_in):
                cost = graph.distance(v_in, v_out) + d
                if v_out not in visited:
                    queue.put((cost, v_out))
                    parent[v_out] = v_in

            visited[v_in] = cost

    return None


def main():
    g1 = Graph()
    #default olarak uzunlukları 1 verdim eşit
    g1.add_edge('s', 'a')
    g1.add_edge('s', 'g')
    g1.add_edge('a', 'c')
    g1.add_edge('a', 'b')
    g1.add_edge('b', 's')
    g1.add_edge('c', 'd')
    g1.add_edge('c', 'g')
    g1.add_edge('d', 'g')
    
    print(ucs('s','g', g1))