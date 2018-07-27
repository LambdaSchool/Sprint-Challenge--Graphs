#!/usr/bin/env python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from random import sample
from sys import argv
from draw import BokehGraph
from graph import Graph, Vertex


def main(num_vertices=15, num_edges=8, draw_components=True, search=0):
    """Build and show random graph."""
    graph = Graph()
    # Add appropriate number of vertices
    for num in range(num_vertices):
        graph.add_vertex(Vertex(label=str(num)))

    # Add random edges between vertices
    for _ in range(num_edges):
        vertices = sample(graph.vertices.keys(), 2)
        # TODO check if edge already exists
        graph.add_edge(vertices[0], vertices[1])

    # if search:
    #     print('yes')
    #     print(graph.find_vert(search))
    test_vert = list(graph.vertices.keys())[search]
    print('rec', graph.graph_rec(test_vert))
    print('dfs', graph.dfs(test_vert))
    bokeh_graph = BokehGraph(graph, draw_components=draw_components)
    bokeh_graph.show()


if __name__ == '__main__':
    if len(argv) == 5:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        DRAW_COMPONENTS = bool(int(argv[3]))
        SEARCH = int(argv[4])
        main(NUM_VERTICES, NUM_EDGES, DRAW_COMPONENTS, SEARCH)
    else:
        main()
