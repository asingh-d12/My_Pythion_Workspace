import time


def factorial_rec(num: int) -> int:
    """
    Return the factorial of number
    :param num: int of which factorial we want
    :return: the actual factorial
    """
    if num == 0:
        return 1
    else:
        return num * factorial_rec(num - 1)


def factorial(num: int) -> int:
    """
    Return the factorial of number
    :param num: int of which factorial we want
    :return: the actual factorial
    """
    if num == 0:
        return 1
    else:
        for k in range(1, num):
            num *= k
        return num


if __name__ == '__main__':
    start_time = time.time()
    for i in range(35):
        print("{} {}".format(i, factorial_rec(i)))
    end_time = time.time()
    print("Time taken = {}seconds".format(end_time - start_time))
