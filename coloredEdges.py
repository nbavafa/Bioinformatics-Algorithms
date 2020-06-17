'''
Nicholas Bavafa
make graph with coloredEdges
'''

import sys

def coloredEdges(P):
    edges = []
    for chromosome in P:
        nodes = chromosomeToCycle(chromosome)
        for i in range(len(chromosome)):
            rtr = "(" + str(nodes[2 * i -1]) + ", " + str(nodes[2 * i]) + ")"
            edges.append(rtr)
    return edges

def chromosomeToCycle(chromosome):
    nodes = [0] * (2 * len(chromosome))
    for j in range(len(chromosome)):
        i = chromosome[j]
        if i > 0:
            nodes[(2 * j) - 1] = 2 * i - 1
            nodes[2 * j] = 2 * i
        else:
            nodes[(2 * j) - 1] = -2 * i
            nodes[2 * j] = -2 * i - 1

    nodesCycle = [nodes[-1]]
    for i in range(len(nodes) - 1):
        nodesCycle.append(nodes[i])

    return nodesCycle
