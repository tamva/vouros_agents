class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        # 0 <- home
        # 1 <- cafe
        # 2 <- cinema

        # ( (Nick, home, delay), (Ann, home, delay), (Tasos, home, delay), (Mary, home, delay), (George, home, delay) )
        self.state = (('N', 0, 0), ('A', 0, 0), ('T', 0, 0), ('M', 0, 0), ('G', 0, 0))


        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position