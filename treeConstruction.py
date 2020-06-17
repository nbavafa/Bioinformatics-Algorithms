'''
Nicholas Bavafa
TreeConstruction
'''

import sys

class Node:
    def __init__(self, index, data, children):
        self.index =  index
        self.data = data.strip()
        self.children = children

    def formatted(x):
        return " -> " + x.index + ":"  + x.data

def treeMerge(node):
    if (len(node.children) == 1):
        node.data = node.data + node.children[0].data
        node.children = node.children[0].children
        treeMerge(node)
    elif len(node.children) == 0:
        return
    else:
        for child in node.children:
            treeMerge(child)

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

def printTree(node):
    print(node.data)
    for child in node.children:
        printTree(child)

def run(suffArr):
    root = trieConstruction(suffArr)
    treeMerge(root)
    for child in root.children:
        printTree(child)
