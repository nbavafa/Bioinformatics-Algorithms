'''
Nicholas Bavafa
finds maxNonBranchingPath
'''

import sys

def maxNonBranchingPath(graph):
    paths = []
    keys = list(graph.keys())
    for key in keys:
        outVertices = graph.get(key)[0]
        if (len(outVertices) != 1):
            if (len(outVertices) > 0):
                for vertex in outVertices:
                    nonBranchingPath = []
                    nonBranchingPath.append(key)
                    nonBranchingPath.append(vertex)
                    currentNode = graph.get(vertex)[0][0]
                    while True:
                        nodes = graph.get(currentNode)[0][0]
                        if len(nodes) != 1:
                            break
                        nextVertex = nodes[0]
                        nonBranchingPath.append(nextVertex)
                        currentNode = nextVertex
                    paths.append(nonBranchingPath)
            del graph[key]


    #all 1-1
    for key in keys:
        if key in graph:
            nonBranchingPath = []
            nonBranchingPath.append(key)
            nextVertex = graph.get(key)[0][0]
            nonBranchingPath.append(nextVertex)
            while True:
                getter = graph.get(nextVertex)
                if getter is None:
                    break
                else:
                    next = getter[0][0]
                    if (next != nonBranchingPath[1]):
                        nonBranchingPath.append(next)
                    del graph[nextVertex]
                    nextVertex = next
            paths.append(nonBranchingPath)

    for path in paths:
        pathString = ""
        for i in range(0, len(path)-1):
            pathString = pathString + path[i] + " -> "
        pathString = pathString + path[-1]
        print(pathString)
