#!/usr/bin/env python
class Node:
    
    def init(self):
        self.results = []
        self.lines = []
        self.multiplication_value = None

    def read_file(self, filepath):
        file = open(filepath, 'r')
        self.lines = file.readlines()

    def traverse(self, right, down):
        lines = self.lines[down::down]
        pos = 0 + right
        result = 0
        for line in lines:
            print(pos)
            if line[pos] == '#':
                result += 1
            pos += right
            if pos > 30:
                pos = pos - 30 - 1
        return result


node = Node()
node.read_file("input.txt")
a = node.traverse(1, 1)
b = node.traverse(3, 1)
c = node.traverse(5, 1)
d = node.traverse(7, 1)
e = node.traverse(1, 2)

sum = a*b*c*d*e
print(sum)