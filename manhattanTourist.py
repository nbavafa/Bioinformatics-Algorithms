'''
Nicholas Bavafa
manhattanTourist problem
'''

import sys

def manhattanTourist(n, m, downEdges, rightEdges):
    matrix = [[0 for x in range(m)] for y in range(n)]
    matrix[0][0] = 0

    for i in range(1, n):
        matrix[i][0] = matrix[i-1][0] + int(downEdges[i-1][0])

    for j in range(1, m):
        matrix[0][j] = matrix[0][j-1] + int(rightEdges[0][j-1])

    for i in range(1, n):
        for j in range(1, m):
            matrix[i][j] = max(matrix[i-1][j] + int(downEdges[i-1][j]), matrix[i][j-1] + int(rightEdges[i][j-1]))

    return matrix[n-1][m-1]
