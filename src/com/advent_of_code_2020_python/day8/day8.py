commands = [line.rstrip() for line in open("Day_8_2020.txt", "r")]


def check_loop(list_commands):
    acc = 0
    pointer = 0
    pointers_seen = []
    while True:
        if pointer in pointers_seen:
            return acc, "In a loop"
        elif pointer >= len(list_commands):
            return acc, "Reached the end"
        else:
            pointers_seen.append(pointer)
        if list_commands[pointer].split()[0] == "nop":
            pointer += 1
        elif list_commands[pointer].split()[0] == "acc":
            acc += int(list_commands[pointer].split()[1])
            pointer += 1
        elif list_commands[pointer].split()[0] == "jmp":
            pointer += int(list_commands[pointer].split()[1])


def swap_command(list_commands, before_swap, after_swap):
    for index in range(0, len(list_commands)):
        if list_commands[index].split()[0] == before_swap:
            list_commands[index] = after_swap + " " + list_commands[index].split()[1]
            acc, run = check_loop(list_commands)
            if run != "In a loop":
                return acc
            list_commands[index] = before_swap + " " + list_commands[index].split()[1]


# print(check_loop(commands))
print(swap_command(commands, "nop", "jmp"))
print(swap_command(commands, "jmp", "nop"))
