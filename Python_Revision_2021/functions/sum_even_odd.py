def sum_eo(n, t):
    if t == "e":
        return sum(range(0, n, 2))
    elif t == "o":
        return sum(range(1, n, 2))

    return -1


if __name__ == "__main__":
    print(sum_eo(10, "e"))
    print(sum_eo(10, "o"))
    print(sum_eo(20, "asd"))
