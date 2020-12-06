input = [line.rstrip() for line in open("Day_3_2020.txt", "r")]
print(input)


def traverse_trees(down, right):
    trees = 0
    length = len(input[0])
    indent = 0
    for i in range(down, len(input), down):
        indent = (indent + right) % length
        if input[i][indent] == '#':
            trees += 1
    return trees


down_list = [1, 1, 1, 1, 2]
right_list = [1, 3, 5, 7, 1]
answer = 1
for i in range(0, len(down_list)):
    answer *= traverse_trees(down_list[i], right_list[i])
print(answer)
