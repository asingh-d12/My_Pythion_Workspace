def sum_numbers(*numbers: float) -> float:
    """
    Gives the sum of all the numbers passed to varia  ble arguments
    :param numbers: all the `int` or `float` numbers
    :return: result in `int` or `float`
    """
    sum_nums = 0
    print(sum(numbers))
    for i in numbers:
        sum_nums += i

    return sum_nums


if __name__ == '__main__':
    print(sum_numbers(1, 2, 3))
    print(sum_numbers(8, 20, 2))
    print(sum_numbers(12.5, 3.147, 98.1))
