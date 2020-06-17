'''
Nicholas Bavafa
Computes reverseComplement
'''

import sys

def reverseComplement(text):
    count = 0
    dict = {
        "A":"T",
        "T":"A",
        "C":"G",
        "G":"C"
    }
    new_string = ""
    for char in text:
        new_string = dict[char] + new_string

    print(new_string)
