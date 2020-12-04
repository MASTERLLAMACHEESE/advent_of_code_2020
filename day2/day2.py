#!/usr/bin/env python

import numbers

class Node():

    def __init__(self):
        self.pol_val = []
        self.pol_let = []
        self.pw = []

        self.final_vals = []
        self.final_lets = []
        self.final_pw = []

        self.count = 0
        self.count_2 = 0

    def read_file(self):
        temp = ""
        f = open("test.txt", "r")
        print("file opened")
        content = f.readlines()
        for line in content:
            temp = line.split(" ")
            self.pol_val.append(temp[0])
            self.pol_let.append(temp[1:2])
            self.pw.append(temp[2:3])

    def format_data(self):
        temp_final_lets = []
        temp_final_lets_2 = []
        temp_final_pw = []
        final_pw = []
        #----getting policy number values-----
        for i in range(len(self.pol_val)):
            temp_val = self.pol_val[i].split("-")
            out_val = self.list_to_int(temp_val)
            self.final_vals.append(out_val)

        #---getting policy letters-----
        for i in range(len(self.pol_let)):
            temp = [elem.strip().split(':') for elem in self.pol_let[i]]
            temp_final_lets.append(temp[0:1])
        for sublist in temp_final_lets:
            for item in sublist:
                temp_final_lets_2.append(item)
        for i in range(len(temp_final_lets_2)):
            temp_2 = temp_final_lets_2[i]
            self.final_lets.append(temp_2[0])

        #---getting policy password----
        for i in range(len(self.pw)):
            temp_3 = [elem.strip().split('\n') for elem in self.pw[i]]
            temp_final_pw.append(temp_3)
        for sublist in temp_final_pw:
            for item in sublist:
                final_pw.append(item)
        for sublist in final_pw:
            for item in sublist:
                self.final_pw.append(item)

    def list_to_int(self, test_list):
        for i in range(0, len(test_list)): 
            test_list[i] = int(test_list[i])
        return test_list

    def get_valid_pw_count(self):
        for i in range(len(self.final_pw)):
            values = self.final_vals[i]
            val_low = values[0]
            val_high = values[1]
            times = self.final_pw[i].count(self.final_lets[i])
            if times >= val_low:
                if times <= val_high:
                    self.count = self.count + 1
        print ("final count part1: ", self.count)


    def print_list(self):
        print ("printing list")
        for i in range(len(self.final_vals)):
            print (self.final_vals[i])
        for i in range(len(self.final_lets)):
            print (self.final_lets[i])
        for i in range(len(self.final_pw)):
            print (self.final_pw[i])

    def get_valid_pw_count_part2(self):
        for i in range(len(self.final_pw)):
            values = self.final_vals[i]
            val_low = values[0] - 1
            val_high = values[1] - 1
            temp_pw = self.final_pw[i]
            if temp_pw[val_low] == self.final_lets[i] and temp_pw[val_high] != self.final_lets[i]:
                self.count_2 = self.count_2 + 1
            if temp_pw[val_low] != self.final_lets[i] and temp_pw[val_high] == self.final_lets[i]:
                self.count_2 = self.count_2 + 1
        print ("Final count part2: ", self.count_2)

def main():
    node = Node()
    print("-----part1------")
    node.read_file()
    node.format_data()
    node.print_list()
    node.get_valid_pw_count()
    print("-----part2------")
    node.get_valid_pw_count_part2()

if __name__ == "__main__":
    main()