import random

answer = 5
to_guess = random.randint(1, 100)
user_input = int(input("Please guess a number between 1 and 10 : "))

if user_input != answer:
    print('Guess Incorrectly.')
    if user_input < answer:
        user_input = int(input("Please guess higher : "))
    else:
        user_input = int(input("Please guess lower : "))

    if user_input == answer:
        print("Guessed correctly the 2nd time!!")
    else:
        print("Sorry, Game Over!!")
else:
    print("You guessed correctly the 1st time!!")
