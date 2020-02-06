
class World:

    def __init__(self, goals):

        # extract wall coords from the world
        self.goals = goals

    def getExits(self):
        return self.goals


    def getActions(self):
        return 1

