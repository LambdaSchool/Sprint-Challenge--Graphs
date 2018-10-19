"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label

    """Trying to make this Graph class work..."""


class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        storage = []
        storage.append(start)
        seen = set()

        while storage:
            current = storage.pop()
            if current not in seen:
                seen.add(current)
                if current == target:
                    break
                storage.extend(self.vertices[current])

        return seen

    def graph_rec(self, start, target=None, seen=None):
        if seen is None:
            seen = set()
        seen.add(start)
        for v in self.vertices[start]:
            if v == target:
                break
            if v not in seen:
                self.graph_rec(v, target, seen)
        return seen

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.graph_rec(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
