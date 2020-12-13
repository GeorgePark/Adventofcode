import re

instructions = [line.rstrip() for line in open("Day_12_2020.txt", "r")]

print(instructions)
pattern = re.compile("([A-Z])([0-9]+)")
heading = 0
moved_vertical = 0
moved_horizontal = 0


def do_move(command, heading, moved_vertical, moved_horizontal):
    if command[0] == "N" or (command[0] == "F" and heading == 3):
        moved_vertical += int(command[1])
    elif command[0] == "S" or (command[0] == "F" and heading == 1):
        moved_vertical -= int(command[1])
    elif command[0] == "E" or (command[0] == "F" and heading == 0):
        moved_horizontal += int(command[1])
    elif command[0] == "W" or (command[0] == "F" and heading == 2):
        moved_horizontal -= int(command[1])
    return heading, moved_vertical, moved_horizontal


for item in instructions:
    command = pattern.match(item).groups()
    if command[0] in ["N", "S", "E", "W", "F"]:
        heading, moved_vertical, moved_horizontal = do_move(command, heading, moved_vertical, moved_horizontal)
    elif command[0] == "R":
        heading = (heading + int(command[1]) / 90) % 4
    else:
        heading = (heading - int(command[1]) / 90) % 4
print(moved_vertical, moved_horizontal)
