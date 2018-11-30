import random as random
import queue as queue

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

        if numUsers <= avgFriendships:
            raise ValueError('numUsers must be greater than avgFriendships!')
            return
        # Add users
        for i in range(numUsers):
            self.addUser(f'User{i}')

        # Create friendships
        for j in range(avgFriendships):
            for i in range(numUsers):
                # userIDs start at index 1
                userID = random.randint(1, numUsers)
                friendID = random.randint(1, numUsers)
                if userID != friendID and userID < friendID:
                    self.addFriendship(userID, friendID)
                    # print('friend added', j)

            # TODO: Find a way to step backwards if userID == friendID

        # print(self.friendships, 'FRIENDSHIPS')


    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        storage = queue.Queue()
        # put the user's friends into the queue
        for friend in self.friendships[userID]:
            storage.put(friend)

        while not storage.empty():
            currentID = storage.get()
            # this will contain a list of all connected friends
            visited[currentID] = []
            if self.friendships[currentID]:
                for friend in self.friendships[currentID]:
                    visited[currentID].append(friend)
                    if friend not in visited:
                        storage.put(friend)
            # print(currentID, "CURRENT ID")

        

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(f'Friendships: \n {sg.friendships} \n')
    connections = sg.getAllSocialPaths(1)
    print(f'Connections: \n{connections}\n')
    print(len(connections))
