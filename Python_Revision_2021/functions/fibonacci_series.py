import time


def fibo_normal(n):
    """Return the nth fibonacci number for the positive number `n`."""
    a = 0
    b = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(2, n+1):
        num = a + b
        a = b
        b = num
    return num


def fibo_rec(n):
    if 0 <= n <= 1:
        return n
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)


if __name__ == '__main__':
    max_num = 40

    start_time = time.time()

    for i in range(max_num):
        fibo_normal(i)
        # print("Fibo({}) == {}".format(i, fibo_normal(i)), end=', ')
    end_time = time.time()
    print()
    print("*" * 50)
    print("Time taken without recursion = {}".format(end_time - start_time))
    print("*" * 50)

    start_time = time.time()
    for i in range(max_num):
        fibo_rec(i)
        # print("Fibo({}) == {}".format(i, fibo_rec(i)), end=', ')
    end_time = time.time()
    print()
    print("*" * 50)
    print("Time taken with recursion = {}".format(end_time - start_time))
    print("*" * 50)
