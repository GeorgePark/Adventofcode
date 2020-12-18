def main():
    input_string = "11,18,0,20,1,7,16"
    numbers = {int(i): index
               for index, i in enumerate(input_string.split(","), start=1)}

    pointer = len(numbers) + 1
    number_to_be_spoken = 0

    while pointer < 2020:

        # Number will have been spoken
        if number_to_be_spoken in numbers.keys():
            next_number = pointer - numbers[number_to_be_spoken]
            numbers[number_to_be_spoken] = pointer
            number_to_be_spoken = next_number
        # First time a number will be spoken
        else:
            numbers[number_to_be_spoken] = pointer
            number_to_be_spoken = 0
        pointer += 1
    print(number_to_be_spoken)


if __name__ == '__main__':
    main()