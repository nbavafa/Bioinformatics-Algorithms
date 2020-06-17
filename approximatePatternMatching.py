'''
Nicholas Bavafa
approximatePatternMatching
'''

import sys

def approximatePatternMatching(text, pattern, d):
    index_list = []
    for x in range(len(text) - len(pattern) + 1):
        if (hammingDistance(str(pattern), text[x:x + len(pattern)]) <= d):
            index_list.append(x)
    print(*index_list)

#Returns list of all neighbors of pattern with mismatch d
def allNeighbors(pattern, d):
    list_neighbors = [pattern]
    list_local = []
    if (d == 0):
        return
    for x in range(len(pattern)):
        if (pattern[x] == "A"):
            list_local.append(pattern[0:x] + "T" + pattern[x + 1:])
            list_local.append(pattern[0:x] + "C" + pattern[x + 1:])
            list_local.append(pattern[0:x] + "G" + pattern[x + 1:])
        if (pattern[x] == "C"):
            list_local.append(pattern[0:x] + "T" + pattern[x + 1:])
            list_local.append(pattern[0:x] + "A" + pattern[x + 1:])
            list_local.append(pattern[0:x] + "G" + pattern[x + 1:])
        if (pattern[x] == "T"):
            list_local.append(pattern[0:x] + "A" + pattern[x + 1:])
            list_local.append(pattern[0:x] + "C" + pattern[x + 1:])
            list_local.append(pattern[0:x] + "G" + pattern[x + 1:])
        else:
            list_local.append(pattern[0:x] + "A" + pattern[x + 1:])
            list_local.append(pattern[0:x] + "C" + pattern[x + 1:])
            list_local.append(pattern[0:x] + "T" + pattern[x + 1:])

        for neighbor in list_local:
            list_neighbors = list_neighbors + allNeighbors(neighbor, d - 1)

    return list_neighbors

def hammingDistance(text1, text2):
    score = len(text1) - len(text2)
    for x in range(0, min(len(text1), len(text2))):
        if (text1[x] != text2[x]):
            score = score + 1
    return score
