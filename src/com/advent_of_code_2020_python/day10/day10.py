jolts = [int(line.rstrip()) for line in open("Day_10_2020.txt", "r")]

jolts.sort()
print(jolts)
count_one_diff = 1
count_three_diff = 1
for index in range(1, len(jolts)):
    if jolts[index] - jolts[index - 1] == 1:
        count_one_diff += 1
    elif jolts[index] - jolts[index - 1] == 3:
        count_three_diff += 1

print(count_one_diff * count_three_diff)


def count_arrangements(jolts_list):
    # Jolt value and number of ways it can be reached with given transformers
    arrangements = {0: 1}
    for jolt in jolts_list:
        # Sum of ways to reach jolt values within 3 jolts, +0 if it is not possible to reach a jolt value
        # You can get the value by all ways you can to the jolt value -1, or by by all ways you can to the jolt value -1
        # or by all ways you can to the jolt value -3. At most a difference of 3 jolts is allowed, thus only 3 back
        # In Python, dict.get(key, default) allows for a default, which is returned if dict[key] is not in the dict
        arrangements[jolt] = arrangements.get(jolt - 1, 0) + arrangements.get(jolt - 2, 0) \
                             + arrangements.get(jolt - 3, 0)
    return arrangements[jolts_list[-1]]


print(count_arrangements(jolts))
