from typing import List

XMAS = [line.rstrip() for line in open("Day_9_2020.txt", "r")]


def find_invalid_number(xmas_list):
    for i in range(25, len(xmas_list)):
        valid = False
        for j in range(1, 26):
            if str(int(xmas_list[i]) - int(xmas_list[i - j])) in xmas_list[i - 25: i - 1]:
                valid = True
        if not valid:
            return xmas_list[i]
    return -1


def sum_to_invalid_number(xmas_list):
    invalid_number = int(find_invalid_number(xmas_list))
    for i in range(0, len(xmas_list)):
        sum_number = 0
        pointer = i
        while sum_number < invalid_number and pointer < len(xmas_list):
            sum_number += int(xmas_list[pointer])
            if sum_number == invalid_number:
                return int(max(xmas_list[i:pointer])) + int(min(xmas_list[i:pointer]))
            else:
                pointer += 1
    return 0


print(find_invalid_number(XMAS))
print(sum_to_invalid_number(XMAS))
