import re

data = [line.rstrip() for line in open("Day_14_2020.txt", "r")]
print(data)


def bitfield(n):
    return ['1' if digit == '1' else '0' for digit in f'{n:36b}']


def version_1():
    values = {}
    for item in data:
        bla = item.split(' = ')
        if bla[0] != 'mask':
            bits = bitfield(int(bla[1]))
            for i in range(0, len(bits)):
                if mask[i] != 'X':
                    bits[i] = mask[i]
            values[bla[0]] = int("".join(str(x) for x in bits), 2)
        else:
            mask = bla[1]
    print(sum(values.values()))


def fill_in_x(s):
    if 'X' not in s:
        return [s]

    i = s.find('X')
    return fill_in_x(s[:i] + '0' + s[i + 1:]) + fill_in_x(s[:i] + '1' + s[i + 1:])


def version_2():
    values = {}
    for item in data:
        bla = item.split(' = ')
        if bla[0] != 'mask':
            mem_address = int(re.search(r"\[(\w+)\]", bla[0]).groups()[0])
            print(mem_address)
            bits = bitfield(mem_address)
            for i in range(0, len(bits)):
                if mask[i] != '0':
                    bits[i] = mask[i]
            mem_values = fill_in_x("".join(bits))
            for mem_value in mem_values:
                values[int("".join(str(x) for x in mem_value), 2)] = int(bla[1])
        else:
            mask = bla[1]
    print(sum(values.values()))


version_2()
