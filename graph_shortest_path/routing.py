#/usr/bin/env python

import sys


# Edge class
class Edge:
    def __init__(self, destination, weight=1):
        self.destination = destination
        self.weight = weight


# Vertex class
class Vertex:
    def __init__(self, value='vertex', color='white', parent=None):
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

        for i in range(len(self.vertices)):
            if self.vertices[i].value == value:
                return self.vertices[i]
            else:
                return None


    def bfs(self, start):
        """
        Breadth-First search from an input starting Vertex
        Should maintain parent references back from neighbors to their parent.

        @param {Vertex} start: The starting vertex
        """
        # applying first edge vertex as parent to vertex "v"
        # for v in self.vertices:
        #     v.parent = v.edges[0].destination
        start = self.find_vertex(start)
        start.color = 'black'
        print(start.color)
        visited = []
        queue = []
        queue.append(start)
        while len(queue) > 0:
            curr_node = queue.pop(0)
            print(f"parent>>>>>>>>>{curr_node.value}")
            for kid in curr_node.edges:
                dest = kid.destination
                print(f"kid>>>>>>>>>{dest.value}")
                if dest.color == 'white':
                    dest.color = 'black'
                    dest.parent = curr_node
                    queue.append(dest)
        queue.clear()


    def output_route(self, start):

        route = []
        queue = []

        if start:
            route.append(start)
            queue.append(start)

            while len(queue) > 0:
                curr_node = queue.pop(0)
                if curr_node.parent:
                    if curr_node.parent not in route:
                        parent_node = curr_node.parent
                        route.append(parent_node)
                        queue.append(parent_node)
        r = ""
        route.reverse()
        for v in range(len(route)):
            if v == 0:
                r += route[v].value
            else:
                r += " --> " + route[v].value
        print(r)

    def route(self, start, end):
        self.bfs(end)
        # self.output_route(start)


# Helper function to add bidirectional edges
def add_edge(start, end):
    start.edges.append(Edge(end))
    end.edges.append(Edge(start))


# if __name__ == '__main__':
#     if len(sys.argv) != 3:
#         print('Usage: routing.py hostA hostB')
#         sys.exit()

graph = Graph()
vertA = Vertex('HostA')
vertB = Vertex('HostB')
vertC = Vertex('HostC')
vertD = Vertex('HostD')
vertE = Vertex('HostE')
vertF = Vertex('HostF')
vertG = Vertex('HostG')
vertH = Vertex('HostH')

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
#
print(f"F, A  {graph.route('HostB', 'HostA')}")
# print(f"E, B  {graph.route(vertE, vertB)}")
# print(f"D, F  {graph.route(vertD, vertF)}")
# print(f"C, H  {graph.route(vertC, vertH)}")


# Look up the hosts passed in from the command line by
# name to see if we can find them.
# hostAVert = graph.find_vertex(sys.argv[1])
#
# if hostAVert is None:
#     print('routing.py: could not find host: ', sys.argv[1])
# sys.exit()
#
# hostBVert = graph.find_vertex(sys.argv[2])
#
# if hostBVert is None:
#     print('routing.py: could not find host: ', sys.argv[2])
# sys.exit()
#
# # Show the route from one Vertex to the other
# graph.route(hostAVert, hostBVert)
