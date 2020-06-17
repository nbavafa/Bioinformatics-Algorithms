'''
Nicholas Bavafa
Computes score between a pattern and a set of strings
'''

import sys

def distanceBetweenPatternAndStrings(pattern, strings):
    score = 0
    for seq in strings:
        score = score + getMinHammingDist(seq, pattern)

    print(score)

def getMinHammingDist(seq, pattern):
    localMinDist = len(pattern) + 1

    for i in range(len(seq) - len(pattern) + 1):
        localD = hammingDistance(pattern, seq[i:i + len(pattern)])
        if (localD < localMinDist):
            localMinDist = localD
    return localMinDist

def hammingDistance(text1, text2):
    score = len(text1) - len(text2)
    for x in range(0, min(len(text1), len(text2))):
        if (text1[x] != text2[x]):
            score = score + 1
    return score
