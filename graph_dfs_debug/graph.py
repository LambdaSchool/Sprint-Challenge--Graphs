"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label, component=-1, color='white'):
        self.label = str(label)
        self.component = component
        self.color = color

    def __repr__(self):
        return 'Vertex: ' + self.label

    """Trying to make this Graph class work..."""
class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        # if vertex in self.vertices:
        #     raise Exception('Error: adding vertex that already exists')
        # if not set(edges).issubset(self.vertices):
        #     raise Exception('Error: cannot have edge to nonexistent vertices')
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):

        # if start not in self.vertices or end not in self.vertices:
        #     raise Exception('Vertices to connect not in graph!')

        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        stack = []
        stack.append(start)
        visited = set()

        while stack:
            current = stack.pop(-1)
            if current == target:
                break
            visited.add(current)
            stack.extend(self.vertices[current] - visited)

        return visited

    def graph_rec(self, start, target=None):
        x = set()
        x.append(start)
        for v in self.vertices[start]:
            graph_rec(v)
        return x

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
