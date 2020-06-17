'''
Nicholas Bavafa
hiearchicalClustering
'''

import sys
import random

class Cluster:
    def __init__(self, indicies, size):
        self.indicies = indicies
        self.size = size

def hiearchicalClustering(data, indexMap):
    usedIndicies = set(())
    newIndicies = set(())

    combined = []
    for i in range(len(data)):
        newIndicies.add(i)

    while (len(newIndicies) > 1):
        mins = getMinimum(data, usedIndicies)

        combined.append(getSingleIdx(mins[:], indexMap))
        # combined.append(mins)

        size1 = indexMap.get(mins[0]).size
        size2 = indexMap.get(mins[1]).size

        row1 = data[mins[0]]
        row2 = data[mins[1]]

        newColumn = []
        for i in range(len(row1)):
            avg = ((data[mins[0]][i] * size1) + (data[mins[1]][i] * size2)) / (size1 + size2)
            newColumn.append(avg)

        for i in range(len(data)):
            temp = data[i][:]
            temp.append(newColumn[i])
            data[i] = temp[:]

        newColumn.append(0)
        data.append(newColumn)

        usedIndicies.add(mins[0])
        usedIndicies.add(mins[1])
        newIndicies.add(len(data) -1)

        newIndicies.remove(mins[0])
        newIndicies.remove(mins[1])

        containedIdx = indexMap.get(mins[0]).indicies + indexMap.get(mins[1]).indicies

        indexMap[len(data) - 1] = Cluster(containedIdx, size1 + size2)

    return combined

def getSingleIdx(arr, indexMap):
    flag = False

    while (flag == False):
        toDelete = []
        toAdd = []
        flag = True
        for elem in arr:
            if indexMap.get(elem).size > 1:
                toDelete.append(elem)
                toAdd += indexMap.get(elem).indicies
                # flag = False

        for elem in toDelete:
            arr.remove(elem)
        for elem in toAdd:
            arr.append(elem)
    return arr


def getIndicies(indexes, indexMap, arr):
    for idx in indexes:
        if (indexMap.get(idx).size == 1):
            arr += indexMap.get(idx).indicies
            return
        else:
            return getIndicies(indexMap.get(idx).indicies, indexMap, arr)

def getMinimum(data, usedIndicies):
    minVal = float("inf")
    minIdx1 = 0
    minIdx2 = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if (i not in usedIndicies and j not in usedIndicies):
                if (i != j):
                    if (data[i][j] < minVal):
                        minIdx1 = i
                        minIdx2 = j
                        minVal = data[i][j]
    return [minIdx1, minIdx2]
