'''
Nicholas Bavafa
Greedy motif searching both with and without pseudo counts
'''

import sys

def greedyMotifSearchPseudo(text, k, t):
    bestMotifs = []
    bestScore = 2147483647 #MAX 32BIT int

    for seq in text:
        bestMotifs.append(seq[0:k])

    for i in range(len(text[0]) - k + 1):
        localMotifs = [text[0][i:i+k]]

        for j in range(1, t):
            profileMatrix = buildProfilePseudo(localMotifs, k)
            localMotifs.append(probableKmer(text[j], k, profileMatrix))

        localScore = scoringFunction(localMotifs, k)
        if bestScore > localScore:
            bestMotifs = localMotifs
            bestScore = localScore

    for motif in bestMotifs:
        print(motif)

def greedyMotifSearch(text, k, t):
    bestMotifs = []
    bestScore = 2147483647 #MAX 32BIT int

    for seq in text:
        bestMotifs.append(seq[0:k])

    for i in range(len(text[0]) - k + 1):
        localMotifs = [text[0][i:i+k]]

        for j in range(1, t):
            profileMatrix = buildProfile(localMotifs, k)
            localMotifs.append(probableKmer(text[j], k, profileMatrix))

        localScore = scoringFunction(localMotifs, k)
        if bestScore > localScore:
            bestMotifs = localMotifs
            bestScore = localScore

    for motif in bestMotifs:
        print(motif)


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

def buildProfilePseudo(list_motifs, k):

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

def buildProfile(list_motifs, k):

    matrix = [[0 for x in range(k)] for y in range(4)]

    for i in range(k):
        dict = {"A": 0,
                "C": 0,
                "G": 0,
                "T": 0 }
        for motif in list_motifs:
            dict[motif[i]] = dict.get(motif[i]) + 1

        matrix[0][i] = (dict["A"] * 1.0/len(list_motifs))
        matrix[1][i] = (dict["C"] * 1.0/len(list_motifs))
        matrix[2][i] = (dict["G"] * 1.0/len(list_motifs))
        matrix[3][i] = (dict["T"] * 1.0/len(list_motifs))

    return matrix
