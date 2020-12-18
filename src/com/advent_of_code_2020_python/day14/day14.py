data = [line.rstrip() for line in open("Day_14_2020.txt", "r")]
print(data)


def bitfield(n):
    return [1 if digit == '1' else 0 for digit in f'{n:36b}']


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

