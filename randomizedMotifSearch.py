'''
Nicholas Bavafa
randomizedMotifSearch
'''

import sys
import random

def randomizedMotifSearch(text, k, t):
    localMotifs = []
    bestMotifs = []
    bestScore = 2147483647 #MAX 32BIT int

    for seq in text:
        random_start = random.randint(0, len(seq) - k)
        localMotifs.append(seq[random_start:random_start + k])

    bestMotifs = localMotifs
    bestScore = scoringFunction(bestMotifs, k)

    while(True):
        profileMatrix = buildProfile(localMotifs, k)

        localMotifs.clear()
        for seq in text:
            localMotifs.append(probableKmer(seq, k, profileMatrix))

        localScore = scoringFunction(localMotifs, k)
        if bestScore > localScore:
            bestMotifs = localMotifs
            bestScore = localScore
        else:
            return (bestScore, bestMotifs)


def scoringFunction(motifs, k):
    score = 0
    consensus = ""
    for i in range(k):
        dict = {"A": 0,
                "C": 0,
                "G": 0,
                "T": 0 }
        for motif in motifs:
            dict[motif[i]] = dict.get(motif[i]) + 1

        consensus = consensus + max(dict, key=dict.get)

    for motif in motifs:
        score = score + hammingDistance(motif, consensus)

    return score

def hammingDistance(text1, text2):
    score = len(text1) - len(text2)
    for x in range(0, min(len(text1), len(text2))):
        if (text1[x] != text2[x]):
            score = score + 1
    return score

def probableKmer(text, k, matrix):
    nucleotide_dict = {"A": 0,
                       "C": 1,
                       "G": 2,
                       "T": 3}

    max_product = 0
    max_kmer = text[0:k]
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        product = 1
        for i in range(len(kmer)):
            product = product * matrix[nucleotide_dict.get(kmer[i])][i]

        if (max_product < product):
            max_product = product
            max_kmer = kmer

    return max_kmer

def buildProfile(list_motifs, k):

    matrix = [[0 for x in range(k)] for y in range(4)]

    for i in range(k):
        dict = {"A": 1,
                "C": 1,
                "G": 1,
                "T": 1 }
        for motif in list_motifs:
            dict[motif[i]] = dict.get(motif[i]) + 1

        matrix[0][i] = (dict["A"] * 1.0/len(list_motifs) + 4)
        matrix[1][i] = (dict["C"] * 1.0/len(list_motifs) + 4)
        matrix[2][i] = (dict["G"] * 1.0/len(list_motifs) + 4)
        matrix[3][i] = (dict["T"] * 1.0/len(list_motifs) + 4)

    return matrix
