'''
Nicholas Bavafa
reconstruct burrow wheeler transform
'''

import sys
import copy

def reconstructBW(BW, BW_indexed):
    dict = {}
    used = set(())

    occurances_sorted = {}
    BW.sort()
    for i in range(len(pattern)):
        char = BW[i]
        if (char not in occurances_sorted):
            occurances_sorted[char] = 1
        else:
            occurances_sorted[char] = occurances_sorted.get(char) + 1
        BW[i] = BW[i] + str(occurances_sorted.get(char))

    for i in range(len(BW)):
        dict[BW_indexed[i]] = BW[i]

    org_string = ""
    prev = dict.get("$1")
    while(prev not in used):
        # org_string += ''.join([i for i in prev if not i.isdigit()])
        org_string += prev + "-"
        used.add(prev)
        prev = dict.get(prev)

    return org_string
