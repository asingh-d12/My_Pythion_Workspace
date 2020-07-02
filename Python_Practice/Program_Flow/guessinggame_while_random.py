import random

max_val = 1000
to_guess = random.randint(1, max_val)

user_input = int(input("Please guess a number between 1 and {} : ".format(max_val)))

attempt_num = 1

# Let's transform this code so that we can run this with while loop
while user_input != to_guess:
    if user_input > to_guess:
        print("Incorrect!! Please guess lower.")
    elif user_input < to_guess:
        print("Incorrect!! Please guess higher.")
    user_input = int(input("Please guess a number between 1 and {} : ".format(max_val)))
    if user_input == 0:
        print("Leaving the game!!")
        attempt_num = 0
        break
    attempt_num += 1

if attempt_num == 1:
    print("Awesome!! You guessed correctly the very first time!!")
elif attempt_num > 1:
    print("You guessed correctly on Attempt Number = {}".format(attempt_num))
