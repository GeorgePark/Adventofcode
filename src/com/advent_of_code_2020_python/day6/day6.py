# As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration forms
# are distributed to the passengers.
#
# The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions for
# which anyone in your group answers "yes". Since your group is just you, this doesn't take very long.
#
# However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each
# of the people in their group, you write down the questions for which they answer "yes", one per line. For example:
#
# abcx
# abcy
# abcz
# In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the
# same question don't count extra; each question counts at most once.)


def anyone_yes(answers):
    total_count = 0
    for item in answers:
        all_chars = set()
        for split_item in item.split():
            print(set(split_item))
            for letter in split_item:
                all_chars.add(letter)
        total_count += len(all_chars)
    print(total_count)


def everyone_yes(answers):
    total_count = 0
    for item in answers:
        all_chars = set("abcdefghijklmnopqrstuwvxyz")
        for split_item in item.split():
            all_chars = set(split_item).intersection(all_chars)
        total_count += len(all_chars)
    print(total_count)


customs_questions = open("Day_6_2020.txt", "r").read().split("\n\n")
anyone_yes(customs_questions)
everyone_yes(customs_questions)
