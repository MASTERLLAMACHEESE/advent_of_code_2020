#!/usr/bin/env python

class Node():
    def __init__(self):
        self.valid_count = 0

##---------part1------------------##

    def read_file(self):
        count_1 = 0
        count_2 = 0
        data_8 = True
        f = open("input.txt", "r")
        print("file opened")
        content = f.readlines()
        for line in content:
            if line == '\n':
                print ("-----------------")
                count_1 = 0
                count_2 = 0
                data_8 = True
            else:
                if "byr" in line:
                    count_1 = count_1 + 1
                    count_2 = count_2 + 1
                if "iyr" in line:
                    count_1 = count_1 + 1
                    count_2 = count_2 + 1
                if "eyr" in line:
                    count_1 = count_1 + 1
                    count_2 = count_2 + 1
                if "hgt" in line:
                    count_1 = count_1 + 1
                    count_2 = count_2 + 1
                if "hcl" in line:
                    count_1 = count_1 + 1
                    count_2 = count_2 + 1
                if "ecl" in line:
                    count_1 = count_1 + 1
                    count_2 = count_2 + 1
                if "pid" in line:
                    count_1 = count_1 + 1
                    count_2 = count_2 + 1
                if "cid" in line:
                    count_1 = count_1 + 1
                if count_1 == 8:
                    self.valid_count = self.valid_count + 1
                    data_8 = False
                    print("Count_1 data_8: ", count_1)
                    print("Count_2 data_8: ", count_2)
                    print ("Valid passport count mid work: ", self.valid_count)
                    count_1 = 0
                    count_2 = 0
                if count_2 == 7 and data_8 == True:
                    self.valid_count = self.valid_count + 1
                    print("Count_1: ", count_1)
                    print("Count_2: ", count_2)
                    print ("Valid passport count mid work: ", self.valid_count)
                    count_1 = 0
                    count_2 = 0
                    data_8 = False
                
            
        print ("Valid passport count: ", self.valid_count)


def main():
    node = Node()
    print("-----part1------")
    node.read_file()
    #node.print_data()
    print("-----part2------")


if __name__ == "__main__":
    main()