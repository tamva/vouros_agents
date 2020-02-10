
from World import World
from LRTAStarAlgorithm import LTRAStarAlgorithm


if __name__ == "__main__":

    delays = (30, 60, 90)

    # (N, A, T, M, G)
    startingPoint = (0, 0, 0, 0, 0)
    targetPoint = (2, 2, 2, 2, 2)

    # instantiate world as an object to be used during value iteration
    w = World( start=startingPoint, end=targetPoint, delays=delays)

    LTRAStarAlgorithm(w)
