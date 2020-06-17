'''
Nicholas Bavafa
compute squaredError
'''

import sys

def squaredError(data, centers, k):
    error = 0

    for point in data:
        nearestCenter = float("inf")
        for center in centers:
            temp = eucledianDist(center, point)
            if (temp < nearestCenter):
                nearestCenter = temp
        error += (nearestCenter**2)

    return round(error / len(data), 3)

def eucledianDist(point1, point2):
    sum = 0
    for i in range(len(point1)):
        sum += (point1[i] - point2[i])**2
    return sum**(0.5)
