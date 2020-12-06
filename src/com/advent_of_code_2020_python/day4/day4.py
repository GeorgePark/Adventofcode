# You can continue to ignore the cid field, but each other field has strict rules about what values are valid for
# automatic validation:
import re


def check_valid_passports(passport_required_fields):
    valid_passport_count = 0
    for passport in split_input:
        passport_items = {field.split(":")[0]: field.split(":")[1] for field in passport.strip().split()}
        if all(key in passport_items.keys() for key in passport_required_fields):
            if check_valid_fields(passport_items):
                valid_passport_count += 1
    print(valid_passport_count)


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
def check_valid_fields(passport_items):
    if not 1920 <= int(passport_items["byr"]) <= 2002:
        return False
    if not 2010 <= int(passport_items["iyr"]) <= 2020:
        return False
    if not 2020 <= int(passport_items["eyr"]) <= 2030:
        return False
    pattern = re.compile("([0-9]+)([a-zA-Z]+)")
    try:
        height = pattern.match(passport_items["hgt"]).groups()
        if str(height[1]) == "cm":
            if not 150 <= int(height[0]) <= 193:
                return False
        elif str(height[1]) == "in":
            if not 59 <= int(height[0]) <= 76:
                return False
        else:
            return False
    except AttributeError:
        return False
    if not re.match(r"#[0-9a-f]+", passport_items["hcl"]) and not len(passport_items["hcl"]) == 7:
        return False
    if not passport_items["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    if not len(passport_items["pid"]) == 9:
        return False
    return True


split_input = open("Day_4_2020.txt", "r").read().split("\n\n")
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
check_valid_passports(required_fields)
