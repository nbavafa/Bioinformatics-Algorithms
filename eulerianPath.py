'''
Nicholas Bavafa
Construct Euler Path
'''

import sys
import random

class Edge:
    def __init__(self, start, end):
        self.start = start.strip()
        self.end =  end.strip()

    def formatted(x):
        return " (" + x.start + " -> " + x.end + ") "

def eulerPath(graph, endingVertex):
    edgeDict = {}

    for key in graph:
        edges = graph.get(key)
        temp= []

        for edge in edges:
            for endVertex in edge:
                new_edge = Edge(key, endVertex)
                temp.append(new_edge)

        edgeDict[key.strip()] = temp

    path = []
    pathIndex = 0
    path.append(endingVertex)
    cycle = []

    while(len(path) != 0):
        edges = edgeDict.get(str(path[pathIndex].strip()))

        if (len(edges) != 0):
            path.append(edges[0].end)
            edges.remove(edges[0])
            edgeDict[pathIndex] = edges

            pathIndex += 1
        else:
            cycle.append(path[pathIndex])
            del path[pathIndex]
            pathIndex -= 1

    cycle = cycle[0:len(cycle)-1]
    cycle.reverse()
    for i in range(len(cycle)-1):
        print(str(cycle[i]) + "->", end="")
    print(cycle[-1])


def getStart(vertexDegree):
    for key in vertexDegree:
        if (vertexDegree.get(key) == -1):
            return key

def getEnd(vertexDegree):
    for key in vertexDegree:
        if (vertexDegree.get(key) == 1):
            return key

def setUp():
    f = open(sys.argv[1], "r")
    graph = {}
    vertexDegree = {}

    for line in f:
        if (line != "\n"):

            components = line.strip().split("->")
            endingVertices = components[1].split(",")
            startVertex = components[0].strip()

            if startVertex in graph:
                list = graph.get(startVertex)

                list.append(endingVertices)
                graph[startVertex] = list
            else:
                graph[startVertex] = [endingVertices]

            if startVertex in vertexDegree:
                vertexDegree[startVertex] = vertexDegree.get(startVertex) - len(endingVertices)
            else:
                vertexDegree[startVertex] = 0 - len(endingVertices)

            for exit in endingVertices:
                exit = exit.strip()
                if exit in vertexDegree:
                    vertexDegree[exit] = vertexDegree.get(exit) + 1
                else:
                    vertexDegree[exit] = 1


    startingVertex = getStart(vertexDegree)

    endingVertex = getEnd(vertexDegree)
    if endingVertex in graph:
        temp = graph.get(endingVertex)
        temp.insert(0, [startingVertex])
        graph[endingVertex] = temp
    else:
        graph[endingVertex] = [[startingVertex]]

    eulerPath(graph, endingVertex)

setUp()
