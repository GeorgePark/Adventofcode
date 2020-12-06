input = [line.rstrip() for line in open("Day_1_2020.txt", "r")]
print(input)


def sum_two(input):
    for i in range(0, len(input) - 1):
        for j in range(i + 1, len(input)):
            if (int(input[i]) + int(input[j])) == 2020:
                print(int(input[i]) * int(input[j]))


def sum_three(input):
    for i in range(0, len(input) - 1):
        for j in range(i + 1, len(input)):
            for k in range(j + 1, len(input)):
                if (int(input[i]) + int(input[j]) + int(input[k])) == 2020:
                    print(int(input[i]) * int(input[j]) * int(input[k]))


sum_three(input)
