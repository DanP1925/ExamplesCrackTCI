def get_char_number(char):
    a = ord('a')
    z = ord('z')
    val = ord(char)
    if a <= val <= z:
        return val - a
    return -1


def toggle(bit_vector, value):
    if value < 0:
        return bit_vector

    mask = 1 << value
    if (bit_vector & mask) == 0:
        bit_vector |= mask
    else:
        bit_vector &= ~mask
    return bit_vector


def create_bit_vector(word):
    bit_vector = 0
    for char in word:
        x = get_char_number(char)
        bit_vector = toggle(bit_vector, x)
    return bit_vector


def check_exactly_one_bit_set(bit_vector):
    return (bit_vector & (bit_vector - 1)) == 0


def is_palindrome_permutation(word):
    bit_vector = create_bit_vector(word)
    return bit_vector == 0 and check_exactly_one_bit_set(bit_vector)


if __name__ == "__main__":
    print("Result " + str(is_palindrome_permutation("tact coa")))
