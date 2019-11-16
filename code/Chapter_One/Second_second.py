def is_permutation(s1, s2):
    # They should have same size
    if len(s1) != len(s2):
        return False

    # Assuming we are using ascii
    letters = [0] * 128

    # Check if has repetitions
    for char in s1:
        letters[ord(char)] += 1
    for char in s2:
        letters[ord(char)] -= 1
        if (letters[ord(char)]) < 0:
            return False
    return True


if __name__ == "__main__":
    print("Result " + str(is_permutation("daniel", "leinad")))
