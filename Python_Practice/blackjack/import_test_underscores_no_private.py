from blackjack import *

print("Hello")

# To understand how we can mess with visible variables in a program that are suppose to be hidden
# We can do something like this
# All this is supposed to not messed with because this is not actually permitted
# Say we destroy something that is created only once at global scale
# blackjack._card_frame.destroy()
# blackjack.play()
# This will muck the whole program up, since the new_game() function won't have the parent Widget to work with

print(globals())
