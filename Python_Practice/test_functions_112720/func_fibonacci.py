# Creating a fibonacci function
def fibonacci(n: int = 10) -> int:
    """Returns the `nth` fibonacci number, for positive number `n`.\n
    `n` has default value of 10 now and this is how we annotate a default parameter"""
    if 0 <= n <= 1:
        # Basically for n = 0 or  n = 1, return n
        return n

    result = None

    a, b = 0, 1
    for i in range(n - 1):
        result = a + b
        a = b
        b = result

    return result


if __name__ == '__main__':
    for i in range(50):
        print("F({}) -> {}".format(i, fibonacci(i)))

    print(fibonacci())
