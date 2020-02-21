#!/usr/bin/env python3

from room import Room
from world import World
import math

import sys
sys.path.append('structs/')
from Queue import Queue
from Stack import Stack

class PathGenerator():
    def __init__(self, worldmap):
        self.worldmap = worldmap

    def generatePath(self):
        superPath = [0]

        playerVisited = set(superPath)
        # while len(playerVisited) != len(self.worldmap.rooms):
        superPath = self.traverseAllIntersectionPaths(0, playerVisited)
        # print(superPath)
        # remove rooms from the end of thisPath until playerVisited is not the same size as total rooms, then undo one step
        choppedValue = superPath.pop()
        while len(set(superPath)) == len(self.worldmap.rooms):
            choppedValue = superPath.pop()
        superPath.append(choppedValue)

        return self.absolutePathToRelative(superPath)

    def traverseAllIntersectionPaths(self, startingIntersection, playerVisited):
        intersectionRoom = self.worldmap.getRoom(startingIntersection)
        complexities = self.intersectionComplexity(startingIntersection, playerVisited)
        complexities = [(roomID, complexity) for roomID, complexity in complexities.items()]

        def byComplexity(elem):
            return elem[1]
        complexities.sort(key=byComplexity)

        thisPath = [startingIntersection]

        for complexity in complexities:
            direction = complexity[0]
            furthest = self.furthestStopInDirection(startingIntersection, direction, playerVisited)
            if furthest in playerVisited:
                continue

            thisPath += self.shortestAbsolutePath(startingIntersection, furthest)[1:]
            visited = set(thisPath)
            playerVisited = playerVisited.union(visited)
            if self.isRoomIntersection(furthest):
                thisPath += self.traverseAllIntersectionPaths(furthest, playerVisited)[1:]
                thisPath += self.shortestAbsolutePath(furthest, startingIntersection)[1:]
            else:
                thisPath += self.shortestAbsolutePath(furthest, startingIntersection)[1:]

        # check for any remaining connections to this intersection
        connections = intersectionRoom.allConnections()
        for connectionKey in connections:
            connection = connections[connectionKey]
            if connection.id not in playerVisited:
                furthest = self.furthestStopInDirection(startingIntersection, connection.id, playerVisited)
                thisPath += self.shortestAbsolutePath(startingIntersection, furthest)[1:]
                visited = set(thisPath)
                playerVisited = playerVisited.union(visited)
                if self.isRoomIntersection(furthest):
                    # print(furthest, "is an intersection")
                    thisPath += self.traverseAllIntersectionPaths(
                        furthest, playerVisited)[1:]
                    thisPath += self.shortestAbsolutePath(
                        furthest, startingIntersection)[1:]
                else:
                    # print(furthest, "is an dead end")
                    thisPath += self.shortestAbsolutePath(furthest, startingIntersection)[1:]
        
        return thisPath


    def furthestStopInDirection(self, startingRoom, directionID, playerVisited):
        prevRoomID = startingRoom
        nextRoomID = directionID

        nextRoom = self.worldmap.getRoom(nextRoomID)
        prevRoom = self.worldmap.getRoom(prevRoomID)
        connections = nextRoom.roomsOtherThan(prevRoom)

        while len(connections) == 1:
            prevRoom = nextRoom
            nextRoomID = connections[0].id
            nextRoom = self.worldmap.getRoom(nextRoomID)
            connections = nextRoom.roomsOtherThan(prevRoom)
            if nextRoomID in playerVisited:
                nextRoomID = prevRoom.id
                break

        return nextRoomID

    def isRoomIntersection(self, roomID):
        room = self.worldmap.getRoom(roomID)
        if room is not None:
            return len(room.allConnections()) > 2
        else:
            return False

    def unvisitedRooms(self, visited):
        rooms = self.worldmap.rooms.copy()
        for room in visited:
            del rooms[room]
        return list(rooms.keys())

    def shortestRelativePath(self, fromRoom, toRoom):
        path = self.shortestAbsolutePath(fromRoom, toRoom)
        return self.absolutePathToRelative(path)

    def shortestAbsolutePath(self, fromRoom, toRoom, visited=None):
        # bfs
        q = Queue()
        q.enqueue([fromRoom])
        if visited is None:
            visited = set()
        visited = visited.copy()

        while q.size() > 0:
            # print(visited)
            path = q.dequeue()
            roomID = path[-1]

            if roomID == toRoom:
                return path
            if roomID not in visited:
                visited.add(roomID)
                room = self.worldmap.getRoom(roomID)
                # print(roomID, room)
                adjacentRooms = [x for x in [room.n_to, room.e_to, room.s_to, room.w_to] if x is not None]
                if len(path) > 1:
                    prevID = path[-2]
                    adjacentRooms = [x for x in adjacentRooms if x.id != prevID]
                    # print("not including previd:", prevID)
                # print(f"adjacent to {roomID}: {adjacentRooms}")
                for adjacent in adjacentRooms:
                    newPath = path.copy()
                    newPath.append(adjacent.id)
                    q.enqueue(newPath)
        return None

    def absolutePathToRelative(self, path):
        relPath = []

        if path is not None:
            for index in range(len(path) - 1):
                roomID = path[index]
                destRoomID = roomID
                offset = 1
                while destRoomID == roomID:
                    destRoomID = path[index + offset]
                    offset += 1
                originRoom = self.worldmap.getRoom(roomID)
                destRoom = self.worldmap.getRoom(destRoomID)
                direction = originRoom.directionOfRoom(destRoom)
                if direction is None:
                    raise IndexError(f"Room {originRoom.id} not connected to Room {destRoom.id}")
                relPath.append(direction)
                # print(f"{destRoomID} from {roomID} = {direction}")
        return relPath

    def deadEndPathsFromRoom(self, roomID=0, visited=None):
        q = Queue()
        q.enqueue([roomID])
        if visited is None:
            visited = set()

        paths = set()
        while q.size() > 0:
            path = q.dequeue()
            roomID = path[-1]
            if roomID not in visited:
                paths.add(tuple(path))
                visited.add(roomID)
                room = self.worldmap.getRoom(roomID)
                adjacentRooms = [x for x in [room.n_to, room.e_to, room.s_to, room.w_to] if x is not None]
                for adjacent in adjacentRooms:
                    newPath = path.copy()
                    newPath.append(adjacent.id)
                    q.enqueue(newPath)

        pathsList = list(paths)
        pathsList.sort(key=len, reverse=True)

        for pathTup in pathsList:
            path = list(pathTup)
            while len(path) > 0:
                path.pop()
                tTuple = tuple(path)
                if tTuple in paths:
                    paths.remove(tuple(path))

        def mySort(elem):
            value = 0
            for i in range(len(elem)):
                div = 0.1 / ((10 * i) + 1)
                value += div
            total = elem[1] + value
            # print(elem[1], "value: ", value, total)
            return total
        pathsList = list(paths)
        pathsList.sort(key=mySort)
        
        return pathsList

    def closestIntersections(self, startRoomID, visited=None):
        if visited is None:
            visited = set()
        visited = visited.copy()

        q = Queue()
        q.enqueue([startRoomID])

        pathsToIntersections = []

        while q.size() > 0:
            path = q.dequeue()
            roomID = path[-1]
            if roomID not in visited or roomID == startRoomID:
                visited.add(roomID)    
                room = self.worldmap.getRoom(roomID)
                adjacentRooms = [x for x in [room.n_to, room.e_to, room.s_to, room.w_to] if x is not None]
                if len(adjacentRooms) > 2 and roomID != startRoomID:
                    pathsToIntersections.append(path)
                    continue
                else:
                    for adjacent in adjacentRooms:
                        newPath = path.copy()
                        newPath.append(adjacent.id)
                        q.enqueue(newPath)
        return pathsToIntersections

    def closestDeadEnds(self, startRoomID, visited=None):
        if visited is None:
            visited = set()
        visited = visited.copy()

        s = Stack()
        s.push([startRoomID])

        deadEnds = []

        while s.size() > 0:
            path = s.pop()
            roomID = path[-1]
            if roomID not in visited:
                visited.add(roomID)
                room = self.worldmap.getRoom(roomID)
                adjacentRooms = [x for x in [room.n_to, room.e_to, room.s_to, room.w_to] if x is not None]
                if len(adjacentRooms) == 1:
                    deadEnds.append(path)
                    continue
                if len(adjacentRooms) > 2 and roomID != startRoomID:
                    continue
                else:
                    for adjacent in adjacentRooms:
                        newPath = path.copy()
                        newPath.append(adjacent.id)
                        s.push(newPath)
        return deadEnds
        

    def intersectionComplexityValue(self, intersectionID, visited=None):
        connections = self.intersectionComplexity(intersectionID, visited)
        value = 0
        for id in connections:
            value += connections[id]
        return value
    
    def intersectionComplexity(self, intersectionID, visited=None):
        if visited is None:
            visited = set()

        visited = visited.copy()
        if intersectionID in visited:
            visited.remove(intersectionID)

        connections = self.worldmap.getRoom(intersectionID).allConnections()
        connectionIDs = [room.id for id, room in connections.items()]
        connections = {}

        loopIDs = connectionIDs
        loops = []
        while len(loopIDs) > 0:
            loopID = loopIDs.pop()
            loopPath = self.roomLoopDestinationFrom(intersectionID, loopID)
            if loopPath is not None:
                loops.append(loopPath)
                if loopPath[-2] in loopIDs:
                    loopIDs.remove(loopPath[-2])


        # check for closest dead ends
        deadEnds = self.closestDeadEnds(intersectionID, visited)
        for deadEnd in deadEnds:
            connections[deadEnd[1]] = (len(deadEnd) - 1) * 2
        # check for closest intersections
        intersections = self.closestIntersections(intersectionID, visited.copy())
        visited.add(intersectionID)

        # remove intersections that are actually parts of loops
        for loop in loops:
            loopStart = loop[0]
            loopEnd = loop[-2]
            for index in range(len(intersections) - 1, -1, -1):
                if intersections[index][1] == loopStart or intersections[index][1] == loopEnd:
                    del intersections[index]

        for intersection in intersections:
            connections[intersection[1]] = 2 * len(intersection) + self.intersectionComplexityValue(intersection[-1], visited)


        if len(loops) > 0:
            baseLoopBranch = loops[0][0]
            connections[baseLoopBranch] = len(self.roomLoopDestinationFrom(intersectionID, baseLoopBranch))
            # for loop in loops:
            #     connections[baseLoopBranch] = connections.get(baseLoopBranch, 0) + len(loop)
        
        return connections

    def typeOfIntersectionConnection(self, intersectionID, directionRoomID):
        pass

    # def intersectionComplexityInDirectionOfLoop(self, intersectionID, directionRoomID, originID, visited=None):
        
    def roomLoopDestinationFrom(self, intersectionRoomID, directionRoomID):
        # dfs
        s = Stack()
        s.push([directionRoomID])
        visited = set([intersectionRoomID])

        while s.size() > 0:
            path = s.pop()
            roomID = path[-1]
            if roomID == intersectionRoomID and len(path) > 3:
                return path
            if roomID not in visited:
                visited.add(roomID)
                room = self.worldmap.getRoom(roomID)
                adjacentRooms = [x for x in [room.n_to, room.e_to, room.s_to, room.w_to] if x is not None]
                for adjacent in adjacentRooms:
                    newPath = path.copy()
                    newPath.append(adjacent.id)
                    s.push(newPath)
        return None

    def findNearestUnfinishedIntersection(self, currentRoomID, playerVisited):
        q = Queue()
        q.enqueue([currentRoomID])

        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            roomID = path[-1]
            if roomID not in visited:
                visited.add(roomID)
                room = self.worldmap.getRoom(roomID)
                adjacentRooms = [x for x in [room.n_to, room.e_to, room.s_to, room.w_to] if x is not None]
                if len(adjacentRooms) > 2:
                    for adjacent in adjacentRooms:
                        if adjacent.id not in playerVisited and path[-1] != path[0]:
                            return path
                for adjacent in adjacentRooms:
                    newPath = path.copy()
                    newPath.append(adjacent.id)
                    q.enqueue(newPath)
        return None


# note direction came from
# if at an intersection
#   calculate shortest route (in directions not explored)
#       check to see if contains intersections, loop with intersections, or simple dead end
#       if has intersections, sum all child costs
#       if a single dead end, cost is 2x
#       if a simple loop, cost is 1x
#   follow shortest route
#   if there are still unvisited rooms
#       if route was simple dead end
#           retrace steps back to previous intersection first
#       find closest unvisited room (bfs)


# recursive alt
