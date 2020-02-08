
class World:

    def __init__(self, goals):

        # extract wall coords from the world
        self.goals = goals

    def getExits(self):
        return self.goals


    def neighbor_states(self, state):
        return 1

