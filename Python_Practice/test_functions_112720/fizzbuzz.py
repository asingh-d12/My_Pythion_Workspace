def fizz_buzz(num: int) -> str:
    """
    Return fizz or buzz or fizz buzz depending upon the number
    :param num:
    :return:
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
    next_num = 0
    while next_num < 100:
        next_num += 1
        print(fizz_buzz(next_num))
        next_num += 1
        correct_ans = fizz_buzz(next_num)
        my_ans = input("Guess what will be next : ")
        if my_ans != correct_ans:
            print("Incorrect answer, the correct ans is {}".format(correct_ans))
            break
    else:
        print("You win!!")
