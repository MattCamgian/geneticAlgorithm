import numpy as np
import random

class road_lanes:
    def __init__(self):
        self.cars = np.random.choice(2, 2000, p=[0.2, 0.8]).tolist()



def traffic_sim(individual):
    if max(individual[4:7]) == 0:
        return 0,0,0,0
    road = [road_lanes(),road_lanes(),road_lanes(),road_lanes()]
    wreck = 0
    passed_intersection = 0
    entered_intersection = 0

    wait = [0,0,0,0]
    state = 0
    endTime = 0
    wait_times = [0]
    num_itr = 500
    endTime = individual[4 + state]
    for time in range(0,num_itr):

        cars = np.zeros([4, 1])

        while endTime == time:
            state = (state + 1) % 4
            seq_times = np.zeros([4,1])
            endTime = time + individual[4+state]
            # if individual[0] == state:
            #     seq_times[0] = individual[4]
            # if individual[1] == state:
            #     seq_times[1] = individual[5]
            # if individual[2] == state:
            #     seq_times[2] = individual[6]
            # if individual[3] == state:
            #     seq_times[3] = individual[7]
            # endTime = time + np.max(seq_times)

        for id in range(0,4):
            if individual[id] == state:
                cars[id] = road[id].cars.pop(0)
                if wait[id] != 0:
                   wait_times.append(wait[id])
                wait[id] = 0

            else:
                if 0 in road[id].cars:
                    idx = road[id].cars.index(0)
                    cars[id] = road[id].cars.pop(idx)
                if road[id].cars[0] == 1:
                    wait[id] = wait[id] + 1

        if (cars[0] or cars[1]) and (cars[2] or cars[3]):
            wreck = wreck +1
        else:
            passed_intersection = passed_intersection + np.sum(cars)
        entered_intersection = entered_intersection + np.sum(cars)

    avg_wait = np.average(np.hstack([wait_times,wait]))
    return passed_intersection, entered_intersection, wreck, avg_wait

traffic_sim([1, 1, 2, 2, 391, 54, 489, 297])
