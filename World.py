
class World:



    def __init__(self, start, end, delays, transitionTimes, stayDurations):

        # (
        # (Nick, home, delay),
        # (Ann, home, delay),
        # (Tasos, home, delay),
        # (Mary, home, delay),
        # (George, home, delay)
        # )
        self.start = (('N', start[0], 0), ('A', start[1], 0), ('T', start[2], 0), ('M', start[3], 0), ('G', start[4], 0))

        # (2, 2, 2, 2, 2)   everyone is at the cinema
        self.end = end

        self.delays = delays

        # transitionTimes = (('N', 30), ('A', 10), ('T', 60), ('M', 60), ('G', 30))
        self.transitionTimes = transitionTimes
        self.stayDurations = stayDurations

    def nextMoves(self, state):

        moves = []
        for person in state:


    def getStartState(self):
        return self.start

    def isEndState(self, s):
        state = (s[0][1], s[1][1], s[2][1], s[3][1], s[4][1])
        return state == self.end
