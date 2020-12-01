#!/usr/bin/env python

import numbers
from itertools import combinations

class Node():

    def __init__(self):
        self.in_list = []
##---------part1------------------##
    def read_in(self):
        f = open("input1.txt", "r")
        print("file opened")
        for line in f:
            try:
                i = int(line)
            except ValueError:
                continue
            self.in_list.append(i)

    def print_list(self):
        print ("printing list")
        for i in range(len(self.in_list)):
            print (self.in_list[i])

    def list_to_int(self):
        [x for x in self.in_list if isinstance(x, numbers.Number)]

    def find_two_nums(self):
        self.list_to_int()
        target_value = 2020
        #print(*self.in_list)
        for i, value in enumerate(self.in_list[:-1]):
            comp = target_value - value
            if comp in self.in_list[i+1:]:
                print("Solution Found: {} and {}, the sum of is {}".format(value, comp,(value+comp)))
                print("{} * {} = {}".format(value, comp, (value*comp)))
##---------part1------------------##

    def find_three_nums(self):
        target_value = 2020
        self.list_to_int()
        arr_size = len(self.in_list)
        # Fix the first element as A[i] 
        for i in range( 0, arr_size-2): 
        # Fix the second element as A[j] 
            for j in range(i + 1, arr_size-1):  
            # Now look for the third number 
                for k in range(j + 1, arr_size): 
                    if self.in_list[i] + self.in_list[j] + self.in_list[k] == target_value: 
                        value_1 = self.in_list[i]
                        value_2 = self.in_list[k]
                        value_3 = self.in_list[j]
                        print("Triplet is", self.in_list[i], ", ", self.in_list[j], ", ", self.in_list[k]," and the sum is {}".format(value_1 + value_2 + value_3))
                        print("The multiplication value is {}".format(value_1 * value_2 * value_3))
                        return True
        # If we reach here, then no  
        # triplet was found 
        return False

def main():
    node = Node()
    print("-----part1------")
    node.read_in()
    #node.print_list()
    node.find_two_nums()
    print("-----part2------")
    node.find_three_nums()

if __name__ == "__main__":
    main()