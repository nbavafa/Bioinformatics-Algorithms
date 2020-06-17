'''
Nicholas Bavafa
compute burrowsWheeler transform
'''

import sys

def cyclicRotations(text):
    bwArr = []
    for i in range(len(text)):
        rotation = text[i:]
        rotation += text[0:i]
        bwArr.append(rotation)
    bwArr.sort()

    bw = ""
    for i in range(len(bwArr)):
        bw += bwArr[i][-1]

    return bw
