#!/usr/bin/env python

class Node():
    def __init__(self):
        self.input = []

##---------part1------------------##

    def read_file(self):
        f = open("input.txt", "r")
        print("file opened")
        content = f.readlines()
        for line in content:
            self.input.append(line)

def main():
    node = Node()
    print("-----part1------")
    node.read_file()
    print("-----part2------")


if __name__ == "__main__":
    main()