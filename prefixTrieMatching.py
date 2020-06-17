'''
Nicholas Bavafa
prefixTrieMatching
'''

import sys

class Node:
    def __init__(self, index, data, children):
        self.index =  index
        self.data = data.strip()
        self.children = children

    def formatted(x):
        return " -> " + x.index + ":"  + x.data

def prefixTrieMatching(text, trie):
    index = 0
    symbol = text[index]
    v = trie
    path = ""
    found = False
    while (True):
        print(path)
        if len(v.children) == 0:
            return path
        for child in v.children:
            if child.data == symbol:
                index += 1
                if (index < (len(text) - 1)):
                    path += symbol
                    symbol = text[index]
                    v = child
                    found = True
                    break
                else:
                    return path
        if (found == False):
            print("no matches found")
            return
        else: found = False


def trieMatching(text, trie):
    for i in range(len(text)):
        prefixTrieMatching(text[i:], trie)

def trieConstruction(patterns):
    root = Node(0, "%", [])
    count = 1
    for pattern in patterns:
        current = root
        for char in pattern:
            found = False
            for edge in current.children:
                if (char == edge.data):
                    current = edge
                    found = True
            if found == False:
                new_node = Node(count, char, [])
                current.children.append(new_node)
                current = new_node
                count += 1
    return root

def printTrie(node):
    for child in node.children:
        print(str(node.index) + "->" + str(child.index) + ":" + child.data)
        printTrie(child)
