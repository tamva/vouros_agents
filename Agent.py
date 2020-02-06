from World import World
from  LRTAStarAlgorithm import LTRAStarAlgorithm


if __name__ == "__main__":

    delays = (30, 60, 90, 120, 180, 240)

    # (Cafe, Cinema)
    stay_durations = (1, 2)

    # (N, A, T, M, G)
    startingPoint = (0, 0, 0, 0, 0)
    targetPoint = (2, 2, 2, 2, 2)
    transition_times = ()

    # instantiate world as an object to be used during value iteration
    w = World(delays)

    # just an object instantion with dummy ctor
    d = LTRAStarAlgorithm(w, startingPoint, targetPoint)




