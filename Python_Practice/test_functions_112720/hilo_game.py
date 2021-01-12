import random

LOW = 1
HIGH = 65535


def guess_the_num(num_to_guess, low, high):
    guesses = 1
    while True:
        guess = (low + high) // 2
        if guess < num_to_guess:
            low = guess + 1
            guesses += 1
        elif guess > num_to_guess:
            high = guess - 1
            guesses += 1
        else:
            return guesses


if __name__ == '__main__':
    max_guesses = 0
    correct_count = 0
    # answer = random.randint(LOW, HIGH)
    for answer in range(LOW, HIGH + 1):
        total_guesses = guess_the_num(answer, LOW, HIGH)
        print("Number to guess = {}\nNumber guessed in {} tries".format(answer, total_guesses))
        # if total_guesses > 10:
        #     break
        print("*" * 100)
        if total_guesses > max_guesses:
            max_guesses, correct_count = total_guesses, 1
        elif total_guesses == max_guesses:
            correct_count += 1

    print("Max Guesses = {}, Correct Count = {}".format(max_guesses, correct_count))
