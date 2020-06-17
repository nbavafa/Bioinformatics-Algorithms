'''
Nicholas Bavafa
A13442275
Homework 9 lloydClustering
'''

import sys

def lloydClustering(data, k):
    randChoice = 0
    used = []

    centers = [tuple(data[i]) for i in range(0, k)]
    prev_centers = []

    while prev_centers[:] != centers[:]:
        #Assign points to centers
        dict= {k:[] for k in centers}
        for point in data:
            closestCenter = assignCenter(centers, point)

            tempArr = dict.get(closestCenter)
            tempArr.append(point)
            dict[closestCenter] = tempArr

        prev_centers = centers[:]
        centers.clear()
        for key in dict:
            centers.append(getNewCenter(dict.get(key)))

    return centers

def getNewCenter(points):
    newCenter = []
    for i in range(len(points[0])):
        sum = 0
        for point in points:
            sum += point[i]
        newCenter.append(round(sum/(len(points)), 3))
    return tuple(newCenter)

def assignCenter(centers, point):
    curr = float("inf")
    currC = None
    for center in centers:
        dist = eucledianDist(center, point)
        if (dist < curr):
            curr = dist
            currC = center
    return tuple(currC)

def eucledianDist(point1, point2):
    sum = 0
    for i in range(len(point1)):
        sum += (point1[i] - point2[i])**2
    return sum**(0.5)
