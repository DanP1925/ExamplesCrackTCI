def get_char_number(char):
    a = ord('a')
    z = ord('z')
    val = ord(char)
    if a <= val <= z:
        return val - a
    return -1


def is_palindrome_permutation(word):
    count_odd = int(0)
    table = [0] * (ord('z') - ord('a') + 1)
    for char in word:
        x = get_char_number(char)
        if x != -1:
            table[x] += 1
            if table[x] % 2 == 1:
                count_odd += 1
            else:
                count_odd -= 1
    return count_odd <= 1


if __name__ == "__main__":
    print("Result " + str(is_palindrome_permutation("tact coa")))
