'''
Nicholas Bavafa
deBruijnComposition
'''
import sys

def deBruijnComposition(text_collection):
    k = len(text_collection[0])

    dict = {}
    for text in text_collection:
        for x in range(0, len(text)-k + 1):
            kmer = text[x:x+k-1]
            next_kmer = text[x+1:x+k]
            if kmer in dict:
                adj_list = dict.get(kmer)
                adj_list.append(next_kmer)

                dict[kmer] = adj_list
            else:
                dict[kmer] = [next_kmer]

    for key in dict:
            print(key + " -> ", end="")
            adj_list = dict.get(key)

            for x in range(len(adj_list) - 1):
                print(adj_list[x] + ",", end="")
            print(adj_list[len(adj_list) -1])
