import random

max_num = 1000

print("Let's start with this game!!\nGuess between 1 and {}".format(max_num))

print("*" * 50)


def get_integer(prompt):
    while True:
        num = input(prompt)
        if num.isnumeric():
            return int(num)
        else:
            print("This is not a number, TRY AGAIN!!")


while True:
    num_to_guess = random.randint(1, max_num)
    print("Number to guess is chosen, Let's continue!!!")

    num_of_chances = 0

    while True:
        num_of_chances += 1
        # num = int(input("Chance number {}, Guess the number : ".format(num_of_chances)))
        num = get_integer("Chance number {}, Guess the number : ".format(num_of_chances))

        if num_to_guess > num:
            print("Guess Higher!!")
        elif num_to_guess < num:
            print("Guess Lower!!")
        else:
            print("Congrats!! You guessed it on your try number = {}".format(num_of_chances))
            break

    print("*" * 100)
    quit_game = input("Press y to quit, Just enter to continue again : ")
    if quit_game == 'y':
        break

    print("*" * 100)
