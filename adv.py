from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# keep track of "reverse" directions
# use this to return to a room with valid moves
backtrack = []
reversed_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# instantiate a set to keep track of visited rooms
visited = set()

# while there are still unvisited rooms
while len(visited) < len(room_graph):
    next_move = None
    # for each exit(neighbor) in the room expressed by (n,s,e,w)
    for exit in player.current_room.get_exits():
        if player.current_room.get_room_in_direction(exit) not in visited:
            next_move = exit
            break
    if next_move is not None:
        traversal_path.append(next_move)
        backtrack.append(reversed_directions[next_move])
        player.travel(next_move)
        visited.add(player.current_room)

    else:
        next_move = backtrack.pop()
        traversal_path.append(next_move)
        player.travel(next_move)

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
