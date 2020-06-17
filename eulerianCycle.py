'''
Nicholas Bavafa
Compute eulerianCycle
'''

import sys
import random

class Edge:
    def __init__(self, start, end):
        self.start = start.strip()
        self.end =  end.strip()

    def formatted(x):
        return " (" + x.start + " -> " + x.end + ") "

def eulerianCycle(graph):
    edgeDict = {}

    for key in graph:
        edges = graph.get(key)
        temp= []

        for edge in edges:
            for endingVertex in edge:
                new_edge = Edge(key, endingVertex)
                temp.append(new_edge)

        edgeDict[key.strip()] = temp

    path = []
    pathIndex = 0
    starting = random.randint(0, len(edgeDict))
    path.append(starting)
    cycle = []

    while(len(path) != 0):
        edges = edgeDict.get(str(path[pathIndex]))

        if (len(edges) != 0):
            path.append(edges[0].end)
            edges.remove(edges[0])
            edgeDict[pathIndex] = edges

            pathIndex += 1
        else:
            cycle.append(path[pathIndex])
            del path[pathIndex]
            pathIndex -= 1
    cycle.reverse()
    for i in range(len(cycle)-1):
        print(str(cycle[i]) + "->", end="")
    print(cycle[-1])
