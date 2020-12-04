#!/usr/bin/env python

class Node():
    def __init__(self):
        self.input = []
        self.tree_count = 0
        self.tree_count_1_1 = 0
        self.tree_count_3_1 = 0
        self.tree_count_5_1 = 0
        self.tree_count_7_1 = 0
        self.tree_count_1_2 = 0
        self.tree_new = []
##---------part1------------------##
    def read_file(self):
        f = open("input.txt", "r")
        print("file opened")
        content = f.readlines()
        for line in content:
            self.input.append(line)

    def find_path(self):
        place_count = 3
        for line in range(len(self.input)):
            if line == 322:
                current_line = self.input[line]
                print ("On last line tree count is:", self.tree_count)
                break
            current_line = self.input[line+1]
            if current_line[place_count] == "#":
                self.tree_count = self.tree_count + 1
                current_line = list(current_line)
                current_line[place_count] = "X"
                current_line = "".join(current_line)
            #print ("line: ", line+1)
            #print ("place count", place_count)
            #print ("current line: ", current_line)
            #print ("tree count: ", self.tree_count)
            #print("-----------")
            place_count = place_count + 3
            if place_count >= 31:
                temp = [int(i) for i in str(place_count)]
                place_count = temp[1]-1

##---------part2------------------##

    def find_path_1_2(self):
        place_count = 1
        for line in range(len(self.input)):
            if (line*2+2) == 322:
                print ("1-2 On last line tree count is:", self.tree_count_1_2)
                break
            current_line = self.input[line*2+2]
            if current_line[place_count] == "#":
                self.tree_count_1_2 = self.tree_count_1_2 + 1
                #current_line = list(current_line)
                #current_line[place_count] = "X"
                #current_line = "".join(current_line)
            #print ("line: ", line*2+2)
            #print ("place count", place_count)
            #print ("current(read) line: ", current_line)
            #print ("tree count: ", self.tree_count_1_2)
            #print("-----------")
            place_count = place_count + 1
            if place_count >= 31:
                temp = [int(i) for i in str(place_count)]
                place_count = temp[1]

    def find_path_single(self,row, place,trees):
        place_count = place
        self.tree_count = 0
        for line in range(len(self.input)):
            if line == 322:
                current_line = self.input[line]
                self.tree_new.append(self.tree_count)
                print (place,"-",row," On last line tree count is:", self.tree_count)
                break
            current_line = self.input[line+row]
            if current_line[place_count] == "#":
                self.tree_count = self.tree_count + 1
                #current_line = list(current_line)
                #current_line[place_count] = "X"
                #current_line = "".join(current_line)
            #print ("line: ", line+1)
            #print ("place count", place_count)
            #print ("current line: ", current_line)
            #print ("tree count: ", self.tree_count)
            #print("-----------")
            place_count = place_count + place
            if place_count >= 31:
                temp = [int(i) for i in str(place_count)]
                place_count = temp[1]-1

    def multiply_treecount(self):
        #print ("Multiplyed tree count is: ", self.tree_count_1_1 * self.tree_count_3_1 * self.tree_count_5_1 * self.tree_count_7_1 * self.tree_count_1_2)
        print ("NEW Multiplyed tree count is: ", self.tree_new[0] * self.tree_new[1] * self.tree_new[2] * self.tree_new[3] * self.tree_count_1_2)

    def print_data(self):
        print ("printing for debug")
        for i in range(len(self.input)):
            print (self.input[i])

def main():
    node = Node()
    print("-----part1------")
    node.read_file()
    #node.print_data()
    #node.find_path()
    print("-----part2------")
    node.find_path_single(1, 1, 0)
    node.find_path_single(1, 3, 1)
    node.find_path_single(1, 5, 2)
    node.find_path_single(1, 7, 3)
    node.find_path_1_2()
    node.multiply_treecount()

if __name__ == "__main__":
    main()