"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return "Vertex: " + self.label

    """Trying to make this Graph class work..."""


class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(start)
        if bidirectional:
            self.vertices[end].add(end)

    def dfs(self, start, target=None):
        x = []
        x.append(start)
        y = set(x)

        while x:
            z = x.pop()
            if z == target:
                break
                # print(f"Target {target}.")
            x.extend(self.vertices[z]) - y

        return y

    def graph_rec(self, start, target=None):
        y = set()
        y.add(start)
        for v in self.vertices[start]:
            self.dfs_recursion(v)
        return y

    def find_components(self):
        y = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex in y:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                y.update(reachable)
        self.components = current_component
