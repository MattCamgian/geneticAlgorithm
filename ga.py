import numpy as np
import random

import matplotlib.pyplot as plt

from trafficSim import traffic_sim
from deap import creator, base, tools, algorithms

creator.create("FitnessMax", base.Fitness, weights=(1.0,-2.0,-1.0))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()


toolbox.register("attr_seq", random.randint, 0, 3)
toolbox.register("attr_light", random.randint, 1, 500)
toolbox.register("individual", tools.initCycle, creator.Individual, (toolbox.attr_seq, toolbox.attr_seq, toolbox.attr_seq, toolbox.attr_seq, toolbox.attr_light,toolbox.attr_light,toolbox.attr_light,toolbox.attr_light))
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def eval(individual):
    passed_intersection, entered_intersection, wreck, avg_wait = traffic_sim(individual)
    return passed_intersection,wreck,avg_wait

toolbox.register("evaluate", eval)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutUniformInt, low=0, up=[3,3,3,3,500,500,500,500] ,indpb=0.15)
toolbox.register("select", tools.selTournament, tournsize=3)

population = toolbox.population(n=100)

NGEN=50
best = []
for gen in range(NGEN):
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
    fits = toolbox.map(toolbox.evaluate, offspring)
    for fit, ind in zip(fits, offspring):
        ind.fitness.values = fit
    best.append(traffic_sim(tools.selBest(population, k=1)[0]))
    print("best: " + str(traffic_sim(tools.selBest(population, k=1)[0])),tools.selBest(population, k=1) )
    print("worst: " + str(traffic_sim(tools.selWorst(population, k=1)[0])),tools.selWorst(population, k=1))
    population = toolbox.select(offspring, k=len(population))


passed_intersection, entered_intersection, wreck, avg_wait = zip(*best)
for value in zip(*best):
    plt.plot(range(0,NGEN),np.array(value))
plt.legend(["passed_intersection", "entered_intersection", "wreck", "avg_wait"])
plt.show()
