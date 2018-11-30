# /usr/bin/env python

import sys


# Edge class
class Edge:
    def __init__(self, destination, weight=1):
        self.destination = destination
        self.weight = weight


# Vertex class
class Vertex:
    def __init__(self, value="vertex", color="white", parent=None):
        self.value = value
        self.edges = []
        # Color of this vertex
        # Used to mark vertices for the traversal algorithm (BFS or DFS)
        self.color = color
        # Parent reference to keep track of the previous node in the
        # graph when traversing through the graph
        self.parent = parent


# Graph class
class Graph:
    def __init__(self):
        self.vertices = []

    def find_vertex(self, value):
        """
        Looks through all the vertices in the graph instance and returns
        the first vertex it finds that matches the `value` parameter.

        Used in the `main` function to look up the vertices passed in
        from the command line.

        @param {*} value: The value of the Vertex to find

        @return None if no such Vertex exists in the Graph.
        @return {Vertex} the found Vertex
        """
        for vertex in self.vertices:
            # print(
            #     f"{value} {vertex.value}, {vertex.edges}, {vertex.color}, {vertex.parent}"
            # )
            if vertex.value == value:
                return vertex
        return None

    def bfs(self, start):
        """
        Breadth-First search from an input starting Vertex
        Should maintain parent references back from neighbors to their parent.

        @param {Vertex} start: The starting vertex
        """
        queue = []
        visited = []

        for edge in start.edges:
            edge.destination.parent = None

        queue.append(start)

        while len(queue) > 0:
            found = queue.pop(0)
            # print(found.edges)

            for edge in found.edges:
                # edge is Edge class, edge.destination is Vertex class
                edge.destination.parent = found
                if edge.destination not in visited:
                    queue.append(edge.destination)

            if found not in visited:
                visited.append(found)

            if len(queue) == 0:
                for i in visited:
                    queue.append(i.value)
                break

        return queue

    def output_route(self, start):
        """
        Print out the route from the start vertex back along its parent
        references (these were set in the `bfs` method)

        @param {Vertex} start: The starting Vertex to follow and print
        """
        searched = self.bfs(start)
        return searched

    def route(self, start, end):
        path = []
        joined = None
        # print(start.value, end.value)

        # BFS to build the parent reference tree
        # self.bfs(end)
        # print(self.bfs(end))

        # print the route from the start Vertex
        # self.output_route(start)
        print(self.output_route(start))
        for node in self.output_route(start):
            if node == end.value:
                path.append(node)
                joined = " --> ".join(path)
                break
            path.append(node)

        print(joined)
        return joined


# Helper function to add bidirectional edges
def add_edge(start, end):
    start.edges.append(Edge(end))
    end.edges.append(Edge(start))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: routing.py hostA hostB")
        sys.exit()

    graph = Graph()
    vertA = Vertex("hostA")
    vertB = Vertex("hostB")
    vertC = Vertex("hostC")
    vertD = Vertex("hostD")
    vertE = Vertex("hostE")
    vertF = Vertex("hostF")
    vertG = Vertex("hostG")
    vertH = Vertex("hostH")

    add_edge(vertA, vertB)
    add_edge(vertB, vertD)
    add_edge(vertA, vertC)
    add_edge(vertC, vertD)
    add_edge(vertC, vertF)
    add_edge(vertG, vertF)
    add_edge(vertE, vertF)
    add_edge(vertH, vertF)
    add_edge(vertH, vertE)

    graph.vertices.append(vertA)
    graph.vertices.append(vertB)
    graph.vertices.append(vertC)
    graph.vertices.append(vertD)
    graph.vertices.append(vertE)
    graph.vertices.append(vertF)
    graph.vertices.append(vertG)
    graph.vertices.append(vertH)

    # Look up the hosts passed in from the command line by
    # name to see if we can find them.
    hostAVert = graph.find_vertex(sys.argv[1])

    if hostAVert is None:
        print("routing.py: could not find host: ", sys.argv[1])
        sys.exit()

    hostBVert = graph.find_vertex(sys.argv[2])

    if hostBVert is None:
        print("routing.py: could not find host: ", sys.argv[2])
        sys.exit()

    # Show the route from one Vertex to the other
    graph.route(hostAVert, hostBVert)
