def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


if __name__ == "__main__":
    print("Result " + str(is_permutation("daniel", "leinad")))
