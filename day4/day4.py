#!/usr/bin/env python

class Node():
    def __init__(self):
        self.input = []

##---------part1------------------##

    def read_file(self):
        f = open("test.txt", "r")
        print("file opened")
        content = f.readlines()
        i = 0
        for line in content:
            self.input.append(line)

    def check_passport(self, line):



    def print_data(self):
        print ("printing for debug")
        for i in range(len(self.input)):
            print (self.input[i])

def main():
    node = Node()
    print("-----part1------")
    node.read_file()
    node.print_data()
    print("-----part2------")


if __name__ == "__main__":
    main()