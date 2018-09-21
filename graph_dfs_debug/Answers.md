Describe the fixes/improvements you made to the Graph implementation here.

Issue 1: No edges connecting the vertices
-Fixed add_edge method by having the start vertex add the end vertex, and the end vertex add the start vertex

Issue 2: All vertices are the same color
-In find_components method it needed to check if was not in visited

Issue 3: Variables in dfs and graph_rec methods are not descriptive
-Changed the following variable names
dfs:
x => stack
y => visited
z => current
graph_rec:
x => queue
v => vertex
