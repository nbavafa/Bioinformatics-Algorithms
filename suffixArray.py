'''
Nicholas Bavafa
construct suffixArray
'''

import sys

def suffixArray(text):
    dict = {}
    suffixes = []
    suffArr = []
    index = len(text) - 1
    for i in range(len(text)):
        kmer = pattern[len(text) - i - 1:]
        dict[kmer] = index
        suffixes.append(kmer)
        index -= 1

    suffixes.sort()
    for suff in suffixes:
        suffArr.append(dict.get(suff))

    return suffArr

def printArr(arr):
    for i in range(len(arr) - 1):
        print(str(arr[i]) + ", ", end="")
    print(arr[-1])
