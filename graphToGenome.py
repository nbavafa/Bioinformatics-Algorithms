'''
Nicholas Bavafa
graphToGenome problem
'''

import sys
import copy

def graphToGenome(genomeGraph):
    P = []
    differences = []
    cycles = []
    for i in range(len(genomeGraph)):
        differences.append(abs(genomeGraph[i-1][1] - genomeGraph[i][0]))

    cycle = []
    for i in range(len(differences)):
        if differences[i] != 1:
            cycles.append(copy.deepcopy(cycle))
            cycle.clear()
            cycle.append(genomeGraph[i][0])
            cycle.append(genomeGraph[i][1])
        else:
            cycle.append(genomeGraph[i][0])
            cycle.append(genomeGraph[i][1])
    cycles.append(copy.deepcopy(cycle))

    for cycle in cycles:
        if (len(cycle) > 0):
            chromosome = cycleToChromosome(cycle)
            P.append(chromosome)
    return P

def cycleToChromosome(cycle):
    chromosome = [0] * int(len(cycle)/2)
    for j in range(len(chromosome)):
        if cycle[(2 * j) - 1] < cycle[2 * j]:
            chromosome[j] = int(cycle[2 * j] / 2)
        else:
            chromosome[j] = int(cycle[(2 * j) - 1] / -2)

    return buildString(chromosome)

def buildString(arr):
    rtr = "("
    if arr[0] > 0:
        rtr += "+"
    rtr += str(arr[0])
    for i in range(1, len(arr)):
        rtr += " "
        if arr[i] > 0:
            rtr += "+"
        rtr += str(arr[i])
    rtr += ")"
    return rtr
