'''
Nicholas Bavafa
soft K-means clustering
'''

import sys

def softKmeans(data, k, beta):
    randChoice = 0
    used = []
    hiddenMatrix = [ [ 0 for i in range(len(data)) ] for j in range(k)]

    centers = [tuple(data[i]) for i in range(0, k)]
    prev_centers = []
    count = 0
    e = 2.71828

    while (count < 100):
        #E step
        for j in range(len(data)):
            denominator = 0
            for i in range(len(centers)):
                denominator += e**(-1 * beta * eucledianDist(centers[i], data[j]))
            for i in range(len(centers)):
                hiddenMatrix[i][j] = (e**(-1 * beta * eucledianDist(centers[i], data[j]))/denominator)

        #M step
        centers.clear()
        for row in hiddenMatrix:
            centers.append(buildCenter(data, row))

        count += 1
    return centers

def buildCenter(data, row):
    point = []

    for j in range(len(data[0])):
        dataColumn = []
        for i in range(len(data)):
            dataColumn.append(data[i][j])
        point.append(dotProduct(row, dataColumn)/sum(row))

    return tuple(point)

def dotProduct(row, column):
    return sum(x * y for x,y in zip(row, column))

def eucledianDist(point1, point2):
    sum = 0
    for i in range(len(point1)):
        sum += (point1[i] - point2[i])**2
    return sum**(0.5)
