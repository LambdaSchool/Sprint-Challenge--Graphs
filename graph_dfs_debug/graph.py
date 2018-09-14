"""
Simple graph implementation compatible with BokehGraph class.
"""
class Stack():
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    
    def size(self):
        return len(self.stack)

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
            self.vertices[start].add(end)

    def dfs(self, start, target=None):
        visited = []
        stack = Stack()
        stack.push(start)
        while stack.size() > 0:
            current = stack.pop()
            if current not in visited:
                if current == target: break
                visited.append(current)
                for next_vert in self.vertices[current]:
                    stack.push(next_vert)
        return visited

    def dfs_recursive(self, start, target=None, visited=None):
        if visited is None:
            visited = []
        visited.append(start)
        for child in self.vertices[start]:
            if child not in visited:
                self.dfs_recursive(child, target, visited)
        return visited

        # x = set()
        # x.add(start)
        # for v in self.vertices[start]:
        #     self.dfs_recursive(v)
        # return x

    def find_components(self):
        visited = set()
        current_component = 0

        i = 0
        test_v = None

        for vertex in self.vertices:
            if i == 3:
                test_v = vertex
            i += 1
        
        for vertex in self.vertices:
            if vertex not in visited:
                # print(self.dfs(vertex, test_v))
                reachable = self.dfs_recursive(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
