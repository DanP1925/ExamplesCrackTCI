def one_edit_replace(first, second):
    found_difference = False
    for i in range(0, len(first)):
        if first[i] != second[i]:
            if found_difference:
                return False
            else:
                found_difference = True
    return True


def one_edit_insert(first, second):
    index1 = 0
    index2 = 0
    while index2 < len(second) and index1 < len(first):
        if first[index1] != second[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True


def is_one_edit_away(first, second):
    if len(first) == len(second):
        return one_edit_replace(first, second)
    elif len(first) + 1 == len(second):
        return one_edit_insert(first, second)
    elif len(first) - 1 == len(second):
        return one_edit_insert(second, first)


if __name__ == "__main__":
    print("Result " + str(is_one_edit_away("pale", "ple")))
    print("Result2 " + str(is_one_edit_away("pale", "bale")))
