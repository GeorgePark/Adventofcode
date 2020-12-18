import re
from collections import defaultdict

bags = [line.rstrip().split("bags contain") for line in open("Day_7_2020.txt", "r")]


def part_1():
    contains_gold = set()
    contains_gold_size = 0
    for item in bags:
        if "shiny gold" in item[1]:
            contains_gold.add(item[0].strip())
    print(contains_gold)

    while len(contains_gold) is not contains_gold_size:
        contains_gold_size = len(contains_gold)
        to_add = set()
        for item in bags:
            for color in contains_gold:
                if color in item[1]:
                    to_add.add(item[0].strip())
        contains_gold.update(to_add)
    print(len(contains_gold))


bags_2 = defaultdict(dict)
for l in open("Day_7_2020.txt", "r"):
    bag = re.match(r'(.*) bags contain', l).groups()[0]
    for count, b in re.findall(r'(\d+) (\w+ \w+) bag', l):
        bags_2[bag][b] = int(count)


def part2():
    def search(bag):
        count = 1
        for s in bags_2[bag]:
            multiplier = bags_2[bag][s]
            count += multiplier * search(s)
        return count
    return search('shiny gold' ) - 1  # Rm one for shiny gold itself


part_1()
print(part2())
