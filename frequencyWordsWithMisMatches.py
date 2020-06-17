'''
Nicholas Bavafa
'''

import sys

def frequentWordsWithMismatch(text, d, k):
    list = []
    freqArray = []
    max = 0
    mismatches = 0
    count = 0

    generateAllKmers("", k, list)
    for pattern in list:
        for x in range(len(text) - k + 1):
            for i in range(len(pattern)):
                if (pattern[i] != text[x+i]):
                    mismatches = mismatches + 1
            if (mismatches <= d):
                count = count + 1
            mismatches = 0
        if (count == max):
            freqArray.append(pattern)
        elif (count > max):
            max = count
            freqArray.clear()
            freqArray.append(pattern)
        count = 0

    print(*freqArray)

def generateAllKmers(pattern, k, list):
    if (k == 0):
        list.append(pattern)
        return

    dna_bases = ['A', 'C', 'G', 'T']
    for x in range(len(dna_bases)):
        add_pattern = pattern + dna_bases[x]
        generateAllKmers(add_pattern, k - 1, list)
