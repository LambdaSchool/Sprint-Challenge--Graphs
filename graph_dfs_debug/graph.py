"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label


class Graph:
    """Trying to make this Graph class work..."""
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def find_vert(self, value):
        vert = [v for v in self.vertices if v.label == str(value)]

        return vert[0]

    def dfs(self, start, target=None):
        stack = []
        stack.append(start)
        found = set()

        while stack:
            cur = stack.pop()
            if cur == target:
                break
            found.add(cur)
            stack.extend(self.vertices[cur] - found)
        # print(found)
        return found

    def graph_rec(self, start, target=None):
        visited = set()
        visited.add(start)

        def rec_helper(curr):
            visited.add(curr)
            for vertex in self.vertices[curr]:
                if vertex not in visited:
                    rec_helper(vertex)
        rec_helper(start)
        return visited

    def find_components(self):
        visited = set()
        current_component = 0
        # print('yes')
        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
