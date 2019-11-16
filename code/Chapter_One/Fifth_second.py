def is_one_edit_away(first, second):
    if len(first) - len(second) > 1:
        return False

    shorter = first if len(first) < len(second) else second
    longer = first if len(first) > len(second) else second

    index1 = 0
    index2 = 0
    found_difference = False
    while index2 < len(second) and index1 < len(first):
        if first[index1] != second[index2]:
            # For insert
            if found_difference:
                return False
            found_difference = True

            # For replacing
            if len(first) == len(second):
                index1 += 1
        else:
            index1 += 1
        index2 += 1
    return True


if __name__ == "__main__":
    print("Result " + str(is_one_edit_away("pale", "ple")))
    print("Result2 " + str(is_one_edit_away("pale", "bale")))
