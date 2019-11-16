def unique_chars(s):
    if has_too_many_chars(s):
        return False
    repeated_values = [None] * 128
    for i in range(0, len(s)):
        char = s[i]
        index = ord(char)
        if repeated_values[index]:
            return False
        else:
            repeated_values[index] = True
    return True


def has_too_many_chars(s):
    return len(s) >= 128


if __name__ == "__main__":
    print("Result " + str(unique_chars("Danieel")))
