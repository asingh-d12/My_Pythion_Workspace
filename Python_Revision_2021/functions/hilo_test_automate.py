def guess_binary(answer, low, high):
    num_of_guesses = 0
    while True:
        mid = (low + high) // 2
        num_of_guesses += 1
        if answer == mid:
            # if num_of_guesses > 10:
            #     print("********")
            return "{} guessed in {} guesses".format(answer, num_of_guesses)
        elif answer > mid:
            low = mid + 1
        else:
            high = mid - 1


if __name__ == '__main__':
    LOW = 1
    HIGH = 1000
    for ans in range(LOW, HIGH + 1):
        print(guess_binary(ans, LOW, HIGH))
