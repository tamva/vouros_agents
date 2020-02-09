
class World:

    is_waiting_at_home = 1
    is_going_to_cafe = 2
    is_waiting_at_cafe = 3
    is_at_cafe = 4
    is_waiting_at_cinema = 5
    is_at_cinema = 6

    is_ready_to_change_state = 1

    isNick = 'N'
    isAnn = 'A'
    isTasos = 'T'
    isMary = 'M'
    isGeorge = 'G'

    transitionTimeForNick = 1
    transitionTimeForGeorge = 1
    transitionTimeForTasos = 2
    transitionTimeForMary = 2

    movieAiringTime = 4
    cinemaStay = 4
    cafeStay = 2


    def __init__(self, start, end, delays,  stayDurations):

        # (
        # (Nick, home, delay, wait),
        # (Ann, home, delay),
        # (Tasos, home, delay),
        # (Mary, home, delay),
        # (George, home, delay)
        # )

        self.start = [(self.isNick, start[0], 0, 0),
                      (self.isAnn, start[1], 0, 0),
                      (self.isTasos, start[2], 0, 0),
                      (self.isMary, start[3], 0, 0),
                      (self.isGeorge, start[4], 0, 0)]

        # (2, 2, 2, 2, 2)   everyone is at the cinema
        self.end = end

        # delays = (30, 60, 90, 120, 180, 240)
        self.delays = delays

        self.time = 0

    def changeTurn(self):
        self.time += 1

    def availableSeatsInCafe(self, state):
        reservedSeats = 0
        for person in state:
            if person[1] == self.is_at_cafe:
                reservedSeats += 1
        return 2 - reservedSeats

    def availableSeatsInCinema(self, state):
        reservedSeats = 0
        for person in state:
            if person[1] == self.is_at_cinema:
                reservedSeats += 1
        return 3 - reservedSeats


    def getStartState(self):
        return self.start

    def isEndState(self, s):
        state = (s[0][1], s[1][1], s[2][1], s[3][1], s[4][1])
        return state == self.end

    def getTransitionStates(self, person, state):

        # multiple cinema rooms
        # transitionTimeForNick
        # (agent, home, delay, wait)

        if person[1] == self.is_waiting_at_home:
            if person[3] == self.is_ready_to_change_state:
                if person[0] == self.isAnn:
                    if self.availableSeatsInCafe(state) > 0:
                        tmp = (person[0], person[1] + 3, person[2], self.cafeStay)  # Ann gets to cafe
                    else:
                        tmp = (person[0], person[1] + 2, person[2] + 1, 1)  # Ann waits to enter cafe

                if person[0] == self.isNick:
                    tmp = (person[0], person[1] + 1, person[2], self.transitionTimeForNick)  # Nick departs for cafe

                if person[0] == self.isTasos:
                    tmp = (person[0], person[1] + 1, person[2], self.transitionTimeForTasos)  # Tasos departs for cafe

                if person[0] == self.isMary:
                    tmp = (person[0], person[1] + 1, person[2], self.transitionTimeForMary)  # Mary departs for cafe

                if person[0] == self.isGeorge:
                    tmp = (person[0], person[1] + 1, person[2], self.transitionTimeForGeorge)  # George departs for cafe

            else:  # still have to waiting at home
                tmp = (person[0], person[1], person[2], person[3] - 1)

        elif person[1] == self.is_going_to_cafe:
            if person[3] == self.is_ready_to_change_state:
                if self.availableSeatsInCafe(state) > 0:
                    tmp = (person[0], person[1] + 2, person[2], self.cafeStay)
                else:  # will have to wait
                    tmp = (person[0], person[1] + 1, person[2] + 1, 1)
            else:  # still getting there
                tmp = (person[0], person[1], person[2], person[3] - 1)

        elif person[1] == self.is_waiting_at_cafe:
            if self.availableSeatsInCafe(state) > 0:
                tmp = (person[0], person[1] + 1, person[2], self.cafeStay)
            else:  # will have to wait
                tmp = (person[0], person[1], person[2] + 1, 1)

        elif person[1] == self.is_at_cafe:
            if person[3] == self.is_ready_to_change_state:
                if self.availableSeatsInCinema(state) > 0 and self.time == self.movieAiringTime:
                    tmp = (person[0], person[1] + 2, person[2], self.cinemaStay)
                else:  # will have to wait
                    tmp = (person[0], person[1] + 1, person[2] + 1, 1)
            else:  # still drinking coffee
                tmp = (person[0], person[1], person[2], person[3] - 1)

        elif person[1] == self.is_waiting_at_cinema:
            if self.availableSeatsInCinema(state) > 0 and self.time == self.movieAiringTime:
                tmp = (person[0], person[1] + 1, person[2], self.cinemaStay)
            else:  # will have to wait
                tmp = (person[0], person[1], person[2] + 1, 1)

        elif person[1] == self.is_at_cinema:
            tmp = (person[0], person[1], person[2], person[3])

        return tmp


    def nextMoves(self, state):

        # state = [('N', 2, 0, 1), ('A', 4, 0, 2), ('T', 1, 2, 1), ('M', 1, 2, 1), ('G', 1, 2, 1)]
        moves = []

        if state == self.getStartState():

            delay = [30, 60, 90]
            location = [0, 1, 2]

            for index_i, pi in enumerate(state):  # remove the pi value from the pj iteration
                for index_j, pj in enumerate(state):
                    if index_i == index_j:
                        continue




                    for loc in location:
                        # return a lsit with two persons
                        tuple1 = (state[index_i][0], loc, 0, 0)
                        tuple2 = (state[index_j][0], loc, 0, 0)
                        # print(tuple2[0])
                        cafe_sum = tuple1[1] + tuple2[1]

                        if cafe_sum == 2:
                            for no_cafe in location:
                                if no_cafe == 1:
                                    continue
                                else:
                                    for a3 in delay:
                                        for a4 in delay:
                                            for a5 in delay:
                                                tuple3 = (0, a3)
                                                tuple4 = (0, a4)
                                                tuple5 = (0, a5)
                                                print([tuple1, tuple2, tuple3, tuple4, tuple5])
                                                moves.append([tuple1, tuple2, tuple3, tuple4, tuple5])
            return moves
        else:

            # state = [('N', 0, 0, 0), ('A', 0, 0, 0), ('T', 0, 0, 0), ('M', 0, 0, 0), ('G', 0, 0, 0)]
            #          (agent, home, delay, wait)
            for person_index, person in enumerate(state):  # remove the person1 value from the person2 iteration
                moves.append(self.getTransitionStates(person, state))

            return [moves]
