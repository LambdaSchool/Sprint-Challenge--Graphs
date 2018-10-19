Describe the fixes/improvements you made to the Graph implementation here.

1. Your add_edges function was not adding the second points to the edges so they wouldn't actually connect. I changed the add_edges function to add ends to directional edges and starts to bidirectional edges.

2. The find_components function was looking for vertices that were list in visited list. I updated the find_components function to check for vertices NOT included in the visited list thereby changing the colors of the vertices not connected to each other.

3. Your two files may be the same from class, but if you have any errors or infinite loops in your graph.py file it can cause problems since all the files work directly with each other.

4. Your code had the loop checking if the target equaled the full stack not just the current node which would cause problems. My reworking of the function removed that issue and had the target checked against the current node.

5. I believe lint is an extension that checks for formatting errors for ease of reading? I'm not exactly sure how to fix this, but you can get the errors to go away simply by disabling the extension from your IDE. But it shouldn't affect your codes ability to work.

6. Having proper names not only let you track them and their jobs easier, but it makes it so others reading your code can read them better too. I unpdated the variable names to be more relevant to what they are.

7. The graph_rec function was not checking for previously visited vertices. And with no target to look for the loop could potentially go on forever. So I changed the recursive function to keep track of visited vertices as well as giving it a check against a target to make sure the loop will eventually end.