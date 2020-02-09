from Node import Node


def movingToCafe(move):
    pass

def movingToCinema(move):
    pass

def isNick(move):
    pass

def isAnn(move):
    pass

def isTasos(move):
    pass

def isMary(move):
    pass

def isGeorge(move):
    pass

def appendMoveToNode(world, node, move, ):
    if isNick(move):
        if movingToCafe(move):
            state = (('N', 1, world.transitionTimes()[0]), node[1], node[2], node[3], node[4])
        else:
            state = (node[0], node[1], node[2], node[3], node[4])
    elif isAnn(move):
        if movingToCafe(move):
            state = (node[0], node[1], node[2], node[3], node[4])
        else:
            state = (node[0], node[1], node[2], node[3], node[4])
    elif isTasos(move):
        if movingToCafe(move):
            state = (node[0], node[1], node[2], node[3], node[4])
        else:
            state = (node[0], node[1], node[2], node[3], node[4])
    elif isMary(move):
        if movingToCafe(move):
            state = (node[0], node[1], node[2], node[3], node[4])
        else:
            state = (node[0], node[1], node[2], node[3], node[4])
    elif isGeorge(move):
        if movingToCafe(move):
            state = (node[0], node[1], node[2], node[3], node[4])
        else:
            state = (node[0], node[1], node[2], node[3], node[4])
    return state

def LTRAStarAlgorithm(world, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    time = 17

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while time <= 24:

        # Get the current node (the one with the lowest f-score)
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if  item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for moves in world.nextMoves(current_node):  # get

            tmpNode = current_node

            for move in moves:
                # state = [ (Nick, home, delay), (Ann, home, delay), (Tasos, home, delay), (Mary, home, delay), (George, home, delay) ]

                if movingToCafe(move) and not(world.availableSeatsInCafe()):
                    break
                if movingToCinema(move) and not (world.availableSeatInCinema()):
                    break

                appendMoveToNode(world, tmpNode, move)

            # Create new node
            new_node = Node(current_node, tmpNode)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = child.getSumDelays(child)

            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            for open_node in open_list:
                open_sum = child.getSumDelays(open_node)
                if g > open_sum:  # and
                    continue

            # Add the child to the open list
            open_list.append(child)

        time += 0.5
