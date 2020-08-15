import time
import random

input("Press Enter to Start!!")
wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = time.time()
input("Press Enter to Stop!!")
end_time = time.time()

# So we are now going to convert epoch times we capture, and convert to local
# time.. then print it in formatted way... check it out
# A Couple of things here:
# 1. localtime() function is taking number of seconds since epoch
# 2. %X is the format - Locale’s appropriate time representation.
# 3. strftime() is a function present in time module, used to format a time
# named tuple to more recognizable format
print("Started @ {}".format(time.strftime("%X", time.localtime(start_time))))
print("Ended @ {}".format(time.strftime("%X", time.localtime(end_time))))
print("Your Reaction Time = {}".format(end_time - start_time))
