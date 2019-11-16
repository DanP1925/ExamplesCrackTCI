def unique_chars(word):
    checker = int(0)
    for i in range(0, len(word)):
        val = ord(word[i]) - ord('a')
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)
    return True


if __name__ == "__main__":
    print("Result " + str(unique_chars("daniel")))
