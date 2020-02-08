from World import World
from  LRTAStarAlgorithm import LTRAStarAlgorithm
from Node import Node


if __name__ == "__main__":

    delays = (30, 60, 90, 120, 180, 240)

    # (Cafe, Cinema)
    stayDurations = (1, 2)

    # (N, A, T, M, G)
    startingPoint = (0, 0, 0, 0, 0)
    targetPoint = (2, 2, 2, 2, 2)

    transitionTimes = (('N', 30), ('A', 10), ('T', 60), ('M', 60), ('G', 30))

    # instantiate world as an object to be used during value iteration
    w = World( start=startingPoint, end=targetPoint, delays=delays, transitionTimes=transitionTimes, stayDurations=stayDurations)

    # just an object instantion with dummy ctor
    d = LTRAStarAlgorithm(w, startingPoint, targetPoint)




