from collections import deque

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # below: a dictionary mapping vertex labels to edges
        self.vertices = {}

    # ---- DAY 1 goal -------
    # below: methods to add to/build the graph

    def add_vertex(self, vertex): # <---- adjacency list building
        self.vertices[vertex] = set()
    
    def add_edge(self, edge, vertex): # <---- edge list building
        if vertex in self.vertices:
            self.vertices[vertex].add(edge)
        else:
            print(f"No {vertex} vertex found")

    def bf_traversal(self, starting_v):
        # FUNCTION RETURNS : "prints the vertices in the order they were visited"
        #create queue - using built in library deque
        q = deque()
        # Enqueue starting vertex
        q.append(starting_v)
        visited = []

        #while the queue is not empty, 
        while q:
            #dequeue a vertex from the queue 
            current_v = q.popleft()
            #...and mark it as visited 
            if current_v not in visited:
                visited.append(current_v)
                #enqueue all of it's children that have not been visited 
                for edge in self.vertices[current_v]:
                    q.append(edge)
        print("BF_TRAVERSAL:")
        print(visited)
    
    def dft_stack(self, starting_v):
        # FUNCTION RETURNS : "prints the vertices in the order they were visited"
        #create stack
        s = deque()
        #push starting vertex
        s.append(starting_v)
        visited = []
        #while the stack is not empty, 
        while s:
            #pop a vertex from the stack
            current_v = s.pop()
            #mark it as visited 
            if current_v not in visited:
                visited.append(current_v)
            #push all of it's children that have not been visited 
                for edge in self.vertices[current_v]:
                    s.append(edge)
        print("DFT_STACK:")
        print(visited)
       

    def dft_recursion(self, starting_v, visited=None):
        #FUNCTION RETURNS : "prints the vertices in the order they were visited"
        if visited is None:
            visited = set()
        
        visited.add(starting_v)
        
        for next in self.vertices[starting_v] - visited:
            dfs_recursion( next, visited)
        
        return visited
       

     # ---- DAY 2 -------
       # BFS FUNCTION RETURNS: "the shortest path from the start node to the destination node."
            # (target near start)for unweighted graphs shortest path = standard breadth first search
            # (target near faraway)for weighted graphs shortest path = Dijkstra Algorithm
            # for weighted graphs with negative weights shortest path = Bellman-Ford Algorithm
            
    def bfs_search(self, starting_v, target_v):
        q = deque()
        # Enqueue starting vertex
        visited = []
        q.append(starting_v)
        print(q)
        #while the queue is not empty, 
        while len(q) > 0:
            #dequeue a vertex from the queue 
            path = q.popleft()
            print ("PATH")
            print (path)
            current_v = (path[-1])
            print("currentv")
            print(current_v)
            #...and mark it as visited 
            if current_v not in visited:
                visited.append(current_v)
                # ---*---- if node == target_node: return true
                if current_v == target_v:
                    print(visited)
                    return path 
                #enqueue all of it's children that have not been visited 
                for edge in self.vertices[current_v]:
                    q.append(edge)
       

    def dfs_search(self, starting_v, target_v):
        s = deque()
        # Enqueue starting vertex
        visited = []
        s.append(starting_v)
        #while the queue is not empty, 
        while len(s) > 0:
            #dequeue a vertex from the queue 
            path = s.pop()
            current_v = path[-1]
            #...and mark it as visited 
            if current_v not in visited:
                visited.append(current_v)
                # ---*---- if node == target_node: return true
                if current_v == target_v:
                    print(visited)
                    return path 
                #enqueue all of it's children that have not been visited 
                for edge in self.vertices[current_v]:
                    s.append(edge)
      