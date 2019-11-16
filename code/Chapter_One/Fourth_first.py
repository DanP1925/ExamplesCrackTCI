def get_char_number(char):
    a = ord('a')
    z = ord('z')
    val = ord(char)
    if a <= val <= z:
        return val - a
    return -1


def build_char_frequency_table(value):
    table = [0] * (ord('z') - ord('a') + 1)
    for char in list(value):
        x = get_char_number(char)
        if x != -1:
            table[x] += 1
    return table


def check_max_one_odd(table):
    found_odd = False
    for count in table:
        if count % 2 == 1:
            if found_odd:
                return False
            found_odd = True
    return True


def is_palindrome_permutation(value):
    table = build_char_frequency_table(value)
    return check_max_one_odd(table)


if __name__ == "__main__":
    print("Result " + str(is_palindrome_permutation("tact coa")))
