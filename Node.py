
class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent, state):
        self.parent = parent

        # 0 <- home
        # 1 <- cafe
        # 2 <- cinema
        # state = ( (Nick, home, delay), (Ann, home, delay), (Tasos, home, delay), (Mary, home, delay), (George, home, delay) )
        self.state = state

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def getSumDelays(self):
        pass


