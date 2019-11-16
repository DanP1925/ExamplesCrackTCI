def urlified(string, true_length):
    array_string = list(string)
    space_count = 0
    for i in range(0, true_length):
        if array_string[i] == ' ':
            space_count += 1
    index = true_length + 2 * space_count
    for i in range(true_length - 1, -1, -1):
        if array_string[i] == ' ':
            array_string[index - 1] = '0'
            array_string[index - 2] = '2'
            array_string[index - 3] = '%'
            index -= 3
        else:
            array_string[index - 1] = array_string[i]
            index -= 1
    return "".join(array_string)


if __name__ == "__main__":
    print("Result " + str(urlified("Mr John Smith    ", 13)))
