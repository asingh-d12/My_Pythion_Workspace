import random

max_num = 1000

ans = random.randint(1, max_num)

n_guess = 0

while True:
    n_guess += 1
    if n_guess > 10:
        print("You lost, all 10 guesses are up")
        break

    num_guess = int(input("Please guess a number between 1 and 1000, you have {} more guesses left : "
                          .format(10 - n_guess)))

    if num_guess < ans:
        print("Please guess higher, Guess again!!")
    elif num_guess > ans:
        print("Please guess lower, Guess again!!")
    else:
        print("You guessed the correct in {} tries!!".format(n_guess))
        break
