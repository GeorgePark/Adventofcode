input = [line.rstrip() for line in open("Day_2_2020.txt", "r")]
print(input)


# Each line gives the password policy and then the password. The password policy indicates the lowest and highest
# number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password
# must contain a at least 1 time and at most 3 times.
def check_passwords(list_of_pw):
    valid_passwords = 0
    for item in list_of_pw:
        split_input = item.split(":")
        min_count = split_input[0].split(" ")[0].split("-")[0]
        max_count = split_input[0].split(" ")[0].split("-")[1]
        letter = split_input[0].split(" ")[1]
        password = split_input[1].strip()
        if int(min_count) <= password.count(letter) < int(max_count) + 1:
            valid_passwords += 1
    print(valid_passwords)


# Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second
# character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of
# these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of
# policy enforcement.
def check_passwords_new_policy(list_of_pw):
    valid_passwords = 0
    for item in list_of_pw:
        split_input = item.split(":")
        pos_1 = int(split_input[0].split(" ")[0].split("-")[0])
        pos_2 = int(split_input[0].split(" ")[0].split("-")[1])
        letter = split_input[0].split(" ")[1]
        password = split_input[1].strip()
        if (letter == password[pos_1 - 1] and letter != password[pos_2 - 1]) or (letter != password[pos_1 - 1]
                                                                                 and letter == password[pos_2 - 1]):
            valid_passwords += 1
    print(valid_passwords)


check_passwords(input)
check_passwords_new_policy(input)
