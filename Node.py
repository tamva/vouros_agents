
class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent, state):
        self.parent = parent

        # 0 <- home
        # 1 <- cafe
        # 2 <- cinema
        # state = [
        #           (Nick, home, delay, wait),
        #           (Ann, home, delay, wait),
        #           (Tasos, home, delay, wait),
        #           (Mary, home, delay, wait),
        #           (George, home, delay, wait)
        #           ]

        self.state = state

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def getSumDelays(child):
        obj_0 = child[0]
        delay_0 = obj_0[1]
        obj_1 = child[1]
        delay_1 = obj_1[1]

        obj_2 = child[2]
        delay_2 = obj_1[1]
        obj_3 = child[3]
        delay_3 = obj_2[1]
        obj_4 = child[4]
        delay_4 = obj_3[1]
        sum = delay_0 + delay_1 + delay_2 + delay_3 + delay_4
        return sum

