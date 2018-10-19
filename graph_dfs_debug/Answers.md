Describe the fixes/improvements you made to the Graph implementation here.

- Got lines to draw by flipping start and end in the add section of the add_edge method

- Modified dfs to out put to y instead of x, x is the queue, y is the visited list. This fix combined with adding not to the visited in find_components allowed the color per matching group to work

- Added vertices check for random gen by using an if statement that checks if the vertex already has a the other in it's edge set

- Fixed search with DFS, now returns True if found, false if not. Did so by modifying the target check to z and returnign true if found. The return at the bottom will return false if hit. Orginal functionality is also preserved 

- Linter errors fixed in graph.py, remember what method set can actually use! 

- renamed x,y,z varible scheme in graph.py to something more readable

- I'm unable to reproduce problem 3 perhaps adding that check fixed it

- I took a look at your recursive function. You needed a way to keep track of what's been visited, so I added the queue param. The queue updates everytime it finds a new value and then returns the queue up to the function above it. The bit on the top is because if queue=set() was there then it would just keep modifying the same set and not reset each time you call it.