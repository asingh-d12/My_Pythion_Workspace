def fizz_buzz(num: int) -> str:
    """
    This is famous fizz-buzz game
    :param num: `int` that will be sent as an argument
    :return:    `fizz` if number is divisible by 3,
                `buzz` if number is divisible by 5,
                `fizz buzz` if num is divisible by  both,
                lastly just return num if it is divisible by none
    """
    if num % 3 == 0 and num % 5 == 0:
        return "fizz buzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return str(num)


if __name__ == '__main__':
    i = 1
    while i <= 100:
        print(fizz_buzz(i))
        i += 1
        pl_res = fizz_buzz(i)
        pl_guess = input()
        # pl_guess = pl_res
        # print(pl_guess)
        if pl_guess != pl_res:
            print("You Lost!!")
            break
        i += 1
    else:
        print("*" * 50)
        print("Congrats!! you win.".center(50))
        print("*" * 50)
