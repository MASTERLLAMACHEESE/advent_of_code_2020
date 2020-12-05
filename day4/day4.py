#!/usr/bin/env python
import re 
class Node():
    def __init__(self):
        self.valid_count = 0
        self.letters = ["a", "b", "c", "d", "e", "f"]

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
                #print ("-----------------")
                count_1 = 0
                count_2 = 0
                data_8 = True
            else:
                if "byr" in line:
                    begin_index = line.find('byr') + 4
                    value_string = line[begin_index:begin_index+4]
                    value = int(value_string)
                    if value >= 1920 and value <= 2002:
                        count_1 = count_1 + 1
                        count_2 = count_2 + 1
                        #print("Count_1: ", count_1)
                        #print("Count_2: ", count_2)
                if "iyr" in line:
                    begin_index = line.find('iyr') + 4
                    value_string = line[begin_index:begin_index+4]
                    value = int(value_string)
                    if value >= 2010 and value <= 2020:
                        count_1 = count_1 + 1
                        count_2 = count_2 + 1
                        #print("Count_1: ", count_1)
                        #print("Count_2: ", count_2)
                if "eyr" in line:
                    begin_index = line.find('eyr') + 4
                    value_string = line[begin_index:begin_index+4]
                    value = int(value_string)
                    if value >= 2020 and value <= 2030:
                        count_1 = count_1 + 1
                        count_2 = count_2 + 1
                        #print("Count_1: ", count_1)
                        #print("Count_2: ", count_2)
                if "hgt" in line:
                    data_str = []
                    data_str_fix = ""
                    i = 0
                    begin_index = line.find('hgt')
                    while True:
                        data_str.append(line[(begin_index+4)+i])
                        if len(line) == (begin_index+i+5):
                            break
                        if line[begin_index+i+4] == "\n":
                            break
                        if line[begin_index+i+5] == " ":
                            break
                        i = i + 1
                    data_str_fix="".join(data_str)
                    #print (data_str_fix)
                    if "in" in data_str_fix:
                        value = int(re.search(r'\d+', data_str_fix).group())
                        if value >= 59 and value <=76:
                            count_1 = count_1 + 1
                            count_2 = count_2 + 1
                            #print ("second", data_str_fix)
                    if "cm" in data_str_fix:
                        value = int(re.search(r'\d+', data_str_fix).group())
                        if value >= 150 and value <= 193:
                            count_1 = count_1 + 1
                            count_2 = count_2 + 1
                            #print ("second", data_str_fix)
                if "hcl" in line:
                    data_str_1 = []
                    data_str_fix_1 = ""
                    i = 0
                    begin_index = line.find('hcl')
                    while True:
                        data_str_1.append(line[(begin_index+4)+i])
                        if len(line) == (begin_index+i+5):
                            break
                        if line[begin_index+i+4] == "\n":
                            break
                        if line[begin_index+i+5] == " " or line[begin_index+i+5] == "\n" :
                            break
                        i = i + 1
                    data_str_fix_1="".join(data_str_1)
                    #print (data_str_1)
                    #print(data_str_fix_1)
                    if len(data_str_fix_1) == 7:
                        if data_str_fix_1[0] == "#":
                            count_1 = count_1 + 1
                            count_2 = count_2 + 1
                if "ecl" in line:
                    begin_index = line.find('ecl') + 4
                    value_string = line[begin_index:begin_index+3]
                    if value_string == "amb " or value_string == "blu" or value_string == "brn" or value_string == "gry" or value_string == "grn" or value_string == "hzl" or value_string == "oth":
                        count_1 = count_1 + 1
                        count_2 = count_2 + 1
                        #print("Count_1: ", count_1)
                        #print("Count_2: ", count_2)
                if "pid" in line:
                    data_str_2 = []
                    data_str_fix_2 = ""
                    i = 0
                    begin_index = line.find('pid')
                    while True:
                        data_str_2.append(line[(begin_index+4)+i])
                        if len(line) == (begin_index+i+5):
                            break
                        if line[begin_index+i+4] == "\n":
                            break
                        if line[begin_index+i+5] == " ":
                            break
                        i = i + 1
                    data_str_fix_2="".join(data_str_2)
                    #print (data_str_2)
                    #print(data_str_fix_2)
                    x = data_str_fix_2.split("\n")
                    #print (x[0])
                    if len(x[0]) == 9:
                        #print ("yeet")
                        count_1 = count_1 + 1
                        count_2 = count_2 + 1
                if "cid" in line:
                    count_1 = count_1 + 1
                if count_1 == 8:
                    self.valid_count = self.valid_count + 1
                    data_8 = False
                    #print("Count_1 data_8: ", count_1)
                    #print("Count_2 data_8: ", count_2)
                    #print ("Valid passport count mid work: ", self.valid_count)
                    count_1 = 0
                    count_2 = 0
                if count_2 == 7 and data_8 == True:
                    self.valid_count = self.valid_count + 1
                    #print("Count_1: ", count_1)
                    #print("Count_2: ", count_2)
                    #print ("Valid passport count mid work: ", self.valid_count)
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