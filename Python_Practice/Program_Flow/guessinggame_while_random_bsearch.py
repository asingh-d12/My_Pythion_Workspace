import random

max_val = 1000
to_guess = random.randint(1, max_val)

print("Number to guess = {}".format(to_guess))

# user_input = int(input("Please guess a number between 1 and {} : ".format(max_val)))

# So, here we are using Binary Search, so instead of taking input from user, let's take how this works
start = 1
end = 1000

mid_pt_guess = (start + end) // 2

attempt_num = 1

# Let's transform this code so that we can run this with while loop
while mid_pt_guess != to_guess:
    if mid_pt_guess > to_guess:
        print("Incorrect!! Please guess lower.")
        end = mid_pt_guess
    elif mid_pt_guess < to_guess:
        print("Incorrect!! Please guess higher.")
        start = mid_pt_guess
    # mid_pt_guess = int(input("Please guess a number between 1 and {} : ".format(max_val)))
    mid_pt_guess = (start + end) // 2
    attempt_num += 1

print("You guessed correctly on Attempt Number = {}".format(attempt_num))
