import time


def factorial_no_rec(num):
    """Calculate factorial num! iteratively"""
    fac = 1
    if num > 1:
        for i in range(2, num + 1):
            fac *= i
    return fac


def factorial_rec(num):
    """Now, let's do factorial recursively"""
    if num == 0 or num == 1:
        # this is the exit condition
        return 1
    else:
        # This is where recursion is happening
        x = num * factorial_rec(num - 1)
        return x


def fibo(n):
    """This is fibonacci series recursively
    f(n) = f(n-1) + f(n-2)
    Quite inefficient
    Iterative approach is better for fibonnaci"""
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


def fib_no_rec(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        a = 0
        b = 1
        i = 2
        while i <= n:
            result = a + b
            a = b
            b = result
            i += 1

    return result


if __name__ == '__main__':
    # print(fibo(20))
    print(fib_no_rec(4))
    # for i in range(36):
    #     print(fibo(i))
    # time_no_rec_start = time.time()
    # for i in range(100):
    #     print("Factorial of {} = {}".format(i, factorial_no_rec(i)))
    # time_no_rec_stop = time.time()
    #
    # print("*" * 100)
    #
    # time_rec_start = time.time()
    # for i in range(100):
    #     print("Factorial of {} = {}".format(i, factorial_rec(i)))
    # time_rec_stop = time.time()
    #
    # print("*" * 100)
    #
    # print("Time taken non recursively = {} seconds".format(time_no_rec_stop - time_no_rec_start))
    # print("Time taken recursively = {} seconds".format(time_rec_stop - time_rec_start))
