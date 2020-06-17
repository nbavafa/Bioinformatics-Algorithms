'''
Nicholas Bavafa
A13442275
conputes kUniversal string
'''

import sys
import random

class Edge:
    def __init__(self, start, end):
        self.start = start.strip()
        self.end =  end.strip()

    def formatted(x):
        return " (" + x.start + " -> " + x.end + ") "

def deBruijnComposition(text_collection):
    k = len(text_collection[0])

    dict = {}
    for text in text_collection:
        for x in range(0, len(text)-k + 1):
            kmer = text[x:x+k-1]
            next_kmer = text[x+1:x+k]
            if kmer in dict:
                adj_list = dict.get(kmer)
                adj_list.append(next_kmer)

                dict[kmer] = adj_list
            else:
                dict[kmer] = [next_kmer]

    composition = []
    for key in dict:
        lineToAdd = key + " -> "
        adj_list = dict.get(key)

        for x in range(len(adj_list) - 1):
            lineToAdd = lineToAdd + adj_list[x] + ","
        lineToAdd = lineToAdd + adj_list[len(adj_list) -1]
        composition.append(lineToAdd)

    return composition

def eulerCycle(graph):
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

    key_list = list(edgeDict.keys())

    starting = key_list[random.randint(0, len(key_list))]
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
    return cycle

def reconstructkmerComp(kmer_list, k):
    dna = kmer_list[0]

    for i in range(1, len(kmer_list)):
        dna = dna + kmer_list[i][k-2]

    return dna

def generateAllBits(k):
    bit_list = bitHelper("", k, [])
    return bit_list

def bitHelper(curr, k, bit_list):
    if (len(curr) == k):
        bit_list.append(curr)
        return
    else:
        bitHelper(curr + "0", k , bit_list)
        bitHelper(curr + "1", k, bit_list)

    return bit_list


def deconstructdeBruijnComposition(f, k):
    debruijnComp = deBruijnComposition(generateAllBits(k))
    graph = {}

    for line in debruijnComp:
        if (line != "\n"):
            components = line.strip().split("->")
            if components[0] in graph:
                list = graph.get(components[0])
                list.append(componets[1].split(","))

                graph[componets[0]] = list
            else:
                graph[components[0]] = [components[1].split(",")]

#Call order
#1) deconstructdeBruijnComposition
#2) eulerCycle
#3) reconstructkmerComp
