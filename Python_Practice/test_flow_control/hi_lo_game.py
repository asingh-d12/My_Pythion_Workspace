max_val = 1000
print("Please think of a number 1 - 1000, and I will try to guess in 10 tries...")
input("Press Enter to Start!!")

# user_input = int(input("Please guess a number between 1 and {} : ".format(max_val)))

# So, here we are using Binary Search, so instead of taking input from user, let's take how this works
start = 1
end = 1000

mid_pt_guess = (start + end) // 2

attempt_num = 1

# Let's transform this code so that we can run this with while loop
while True:
    print("My guess is {}. Is this your number??".format(mid_pt_guess))
    h_or_l = input("Please enter h/high/higher if your number is higher than my guess.\n"
                   "Please enter l/low/lower if your number is lower than my guess.\n"
                   "Just Press Enter if this is your number.\nPlease Enter : ")
    if 'l' in h_or_l.casefold():
        end = mid_pt_guess - 1
    elif 'h' in h_or_l.casefold():
        start = mid_pt_guess + 1
    else:
        print("*" * 100)
        print("Awesome, your number is {}, and it took me {} attempts to guess it.".format(mid_pt_guess, attempt_num))
        break
    mid_pt_guess = (start + end) // 2
    attempt_num += 1
