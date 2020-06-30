import random

answer = 5
to_guess = random.randint(1, 100)
user_input = int(input("Please guess a number between 1 and 10 : "))

if user_input > answer:
    print('You guessed higher, you get 1 more chance.')
    user_input = int(input("Please guess number lower than {} : ".format(user_input)))
    if user_input == answer:
        print("You guessed correctly the 2nd time!!")
    else:
        print("No good!!")
elif user_input < answer:
    print('You guessed lower.')
    user_input = int(input("Please guess number higher than {} : ".format(user_input)))
    if user_input == answer:
        print("You guessed correctly the 2nd time!!")
    else:
        print("No good!!")
else:
    print('You guessed correct!!')
