# Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified
# like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".
#
# The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0
# through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows;
# the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next
# letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.
import math
import re


def calc_position(low, high, sequence, pointer, lower):
    if low == high:
        return low
    if sequence[pointer] == lower:
        pointer += 1
        result = calc_position(low, math.ceil((high + low) / 2) - 1, sequence, pointer, lower)
    else:
        pointer += 1
        result = calc_position(math.floor((high + low) / 2) + 1, high, sequence, pointer, lower)
    return result


# Find all ids from boarding passes
pattern = re.compile("([FB]+)([LR]+)")
boarding_passes = [line.rstrip() for line in open("Day_5_2020.txt", "r")]
print(boarding_passes)
all_ids = []
for boarding_pass in boarding_passes:
    try:
        height = pattern.match(boarding_pass).groups()
        row = calc_position(0, 127, height[0], 0, "F")
        col = calc_position(0, 7, height[1], 0, "L")
        all_ids.append(row * 8 + col)
    except AttributeError:
        print("Nope")
print(max(all_ids))

# Find my seat

# generated_ids = []
# for i in range(0, 127):
#     for j in range(0, 7):
#         generated_ids.append(i * 8 + j)
# print(set(generated_ids) - set(all_ids))

for i in range(0, 1023):
    if i-1 in all_ids and i+1 in all_ids and i not in all_ids:
        print(i)
        break
