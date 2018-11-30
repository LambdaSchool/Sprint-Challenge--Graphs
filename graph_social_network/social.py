from random import shuffle
import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        userList=[]

        for user in range(0, numUsers):
            self.addUser(user)
            userList.append(user)

        friendSpread = []
        for userID in userList:
            for friendID in userList:
                if(userID < friendID):
                    friendSpread.append([userID, friendID])
        
        shuffle(friendSpread)
        slicedFriends = friendSpread[0: numUsers]

        for friend in slicedFriends:
            self.addFriendship(friend[0] + 1, friend[1]+1)

        
        

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        visited[userID] = [userID]
        visited = self.exploreNode(
            self.friendships, userID, self.friendships[userID], visited)
        visitedCopy = sorted(
            visited, key=lambda k: len(visited[k]), reverse=False)
        visitedDictionary = {}

        for visitedID in visitedCopy:
            visitedDictionary[visitedID] = visited[visitedID]

        return visitedDictionary

    def exploreNode(self, graph, start, node, visited):
        for friend in node:
            if(friend not in visited):
                visited[friend] = list(
                    self.shortest_path(graph, start, friend))
                visited = self.exploreNode(
                    graph, start, graph[friend], visited)
        return visited

    def bfs_paths(self, graph, start, goal):
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next in graph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path +[next]))

    def shortest_path(self, graph, start, goal):
        if(start == goal):
            return [start]
        try:
            return next(self.bfs_paths(graph, start, goal))
        except StopIteration:
            return None

        
    


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
