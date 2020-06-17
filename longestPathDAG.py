'''
Nicholas Bavafa
computes longest path in a DAG
'''

import sys

class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end =  end
        self.weight = int(weight)

    def formatted(x):
        return " (" + str(x.start) + " --[" + str(x.weight) + "]-> " + str(x.end)+ ") "

def topoSort(graph):
    visitedSet = set(())
    order = []
    for key in graph:
        if key not in visitedSet:
            topoSortHelper(key, graph, visitedSet, order)
    return order[::-1]

def topoSortHelper(vertex, graph, visitedSet, order):
    visitedSet.add(vertex)
    if graph.get(vertex) != None:
        for edge in graph.get(vertex):
            if edge.end not in visitedSet:
                topoSortHelper(edge.end, graph, visitedSet, order)

    order.append(vertex)

def longestPath(graph, source, sink, edgeCount):
    s = [-float('inf') for x in range(edgeCount)]
    s[int(source)] = 0
    order = topoSort(graph)

    totals = []
    max_index = -1
    current_index = -1

    path = []
    weight = 0
    inPath = False
    for i in range (len(order)-1):
        path.append(order[i])
        if order[i] in graph:
            for edge in graph.get(order[i]):
                if edge.end == order[i+1]:
                    weight += edge.weight
                    inPath = True
                    break
            if (inPath == False):
                lastEdge = graph.get(order[i])[0]
                path.append(lastEdge.end)
                weight += lastEdge.weight

        if (inPath == False):
            current_index += 1
            totals.append([weight, path])
            if (max_index == -1):
                max_index = current_index
            elif (totals[max_index][0] < weight):
                max_index = current_index
            weight = 0
            path = []

        inPath = False
    for pathers in totals:
        print(pathers)
    return totals[max_index]

def getZeros(inDegree):
    list = []
    for key in inDegree:
        if (inDegree.get(key) == 0):
            list.append(key)
    return key

def setUp():
    f = open(sys.argv[1], "r")

    sourceNode = f.readline().strip()
    sinkNode = f.readline().strip()

    dict = {}
    inDegree = {}
    edgeCount = 0
    for line in f:
        if (line != "\n"):
            lineArgs = line.split("->")
            lastArg = lineArgs[1].split(":")
            outVertex = int(lastArg[0].strip())
            inVertex = int(lineArgs[0].strip())
            edgeCount += 1
            if (int(int(lastArg[1])) <= 0):
                pass
            else:
                if inVertex not in dict:
                    dict[inVertex] = [Edge(int(lineArgs[0]), int(lastArg[0]), int(int(lastArg[1])))]
                else:
                    temp_list = dict.get(inVertex)
                    temp_list.append(Edge(int(lineArgs[0]), int(lastArg[0]), int(int(lastArg[1]))))
                    dict[inVertex] = temp_list

                if lineArgs[0] not in inDegree:
                    inDegree[lineArgs[0]] = 0
                if lastArg[0] not in inDegree:
                    inDegree[lastArg[0]] = 1
                else:
                    temp = inDegree.get(lastArg[0])
                    inDegree[lastArg[0]] = temp + 1

    del inDegree[sourceNode]

    list_prune = getZeros(inDegree)
    for edge in list_prune:
        if edge in dict:
            del dict[edge]

    return longestPath(dict, int(sourceNode), int(sinkNode), edgeCount)

setUp()
