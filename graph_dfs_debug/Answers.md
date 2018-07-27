Describe the fixes/improvements you made to the Graph implementation here.

1. Nothing seems to connect, my edges aren't showing up.

* in the add_edges method, you were pointing the start to the start and the end to the end.

2. All the vertexes are the same color.  They're supposed to be different colors
if they're not connected, and right now none of them are.

* in the dfs method, you're returning x which is your stack. you need to be returning a list of items you've found. you've created a variable y but never used it. also to reduce looking at the same item multiple times. we want to remove items we've already looked at from the stack. you can do this by subtracting the the edges set() on the currect vert from the found items.
* in the find_compoents method, the (if vertex in visited) should be (if vertex not in visited). when the method is call visited is empty, so you'll never reach the dfs call that adds items to the visited.

3. Sometimes I do something and when I run `python graph_demo.py` it just takes
forever, even though my `draw.py` and `graph_demo.py` are totally just the same
as from class.

* 

4. I wanted to let it find a target vertex, but even back when it did kinda run
this part didn't really work.

* add a find_vert method. 

5. My editor sure is complaining a lot about something called "lint."

* install a linter

6. I keep losing track of my variables, I guess I should name them better?

* variable names x and y are confusing. the norm in a dfs is to call you list of items you need to look at a stack. 


7. I also tried to do it with recursion instead of a stack, in `graph_rec`, but I
got even more stuck. It was running forever so I tried adding a thing to keep
track of vertices, and now I just get an error message. Please try to fix this
too if you can, or at least give me some pointers on what I should be doing.

* this method resets your x variable every time it calls it's self. i added a nested method