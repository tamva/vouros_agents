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

def LTRAStarAlgorithm(world):

    # Create start and end node
    s = [
         (world.isNick,     world.is_at_home, 0, 0),
         (world.isAnn,      world.is_at_home, 0, 0),
         (world.isTasos,    world.is_at_home, 0, 0),
         (world.isMary,     world.is_at_home, 0, 0),
         (world.isGeorge,   world.is_at_home, 0, 0)
         ]

    start_node = Node(None, s)
    start_node.g = start_node.h = start_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while world.time <= 14:

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
        if world.is_end_state(current_node.state):
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for move in world.nextMoves(current_node.state):  # get

            # Create new node
            new_node = Node(current_node, move)

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

        world.change_turn()
