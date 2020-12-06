#!/usr/bin/env python

class Node():
    def __init__(self):
        self.input = []
        self.row_bin_value = []
        self.col_bin_value = []
        self.row_values = []
        self.col_values = []
        self.seat_id_val = []
        

    def read_input(self):
        f = open("input.txt", "r")
        print("file opened")
        content = f.readlines()
        for line in content:
            temp = line
            split_temp = [char for char in temp]
            #split_temp[10]=""
            #split_temp.pop()
            self.input.append(split_temp)

    def get_seat_binary(self):
        for content in range(len(self.input)):
            seat_id = self.input[content]
            value_row = []
            value_col = []
            for x in range(len(seat_id)):
                letter = seat_id[x]
                if letter == "F":
                    value_row.append(0)
                if letter == "B":
                    value_row.append(1)
                if letter == "L":
                    value_col.append(0)
                if letter == "R":
                    value_col.append(1)
            #print("row: ", value_row, " col: ", value_col)
            col_bin_value = int("".join(map(str, value_col)))
            row_bin_value = int("".join(map(str, value_row)))
            self.col_bin_value.append(col_bin_value)
            self.row_bin_value.append(row_bin_value)
            #print(self.row_bin_value)
            #print(self.col_bin_value)

    def get_decimal(self):
        for x in range(len(self.col_bin_value)):
            self.col_values.append(self.binary_to_decimal(self.col_bin_value[x]))
        for x in range(len(self.row_bin_value)):
            self.row_values.append(self.binary_to_decimal(self.row_bin_value[x]))

    def format_value(self):
        for x in range(len(self.row_values)):
            self.seat_id_val.append(self.row_values[x] * 8 + self.col_values[x])

    def print_max_val(self):
        print ("Highest value: ", max(self.seat_id_val))

    def binary_to_decimal(self, binary):
        binary1 = binary 
        decimal, i, n = 0, 0, 0
        while(binary != 0): 
            dec = binary % 10
            decimal = decimal + dec * pow(2, i) 
            binary = binary//10
            i += 1
        return decimal

    def get_missing_seat(self):
        res = [ele for ele in range(max(self.seat_id_val)+1) if ele not in self.seat_id_val]
        print("The list of missing elements : " + str(res))  

def main():
    node = Node()
    print("-----part1------")
    node.read_input()
    node.get_seat_binary()
    node.get_decimal()
    node.format_value()
    node.print_max_val()
    print("-----part2------")
    node.get_missing_seat()

if __name__ == "__main__":
    main()