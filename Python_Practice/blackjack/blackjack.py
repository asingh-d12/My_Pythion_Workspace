import tkinter
from blackjack_loadcards import load_cards, deal_cards, score_hand

# importing random to randomize/shuffle the cards
import random


def deal_dealer():
    # Dealer only draws cards when player holds
    # So, we can make final checks here to check who actually wins the game
    # So far, in deal_player.. there is only 1 check to check if player is busted..
    # in that case of which dealer wins by default

    dealer_score = score_hand(dealer_hand)
    # Here we are going to keep on dealing cards to dealer until reaches >=17
    # Basically, player will only call for dealer to start getting cards once he holds
    # so, disabling player button
    player_button.configure(state="disabled")

    # we are getting player_score here to check who wins
    player_score = score_hand(player_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_cards(dealer_card_frame, deck))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)
        if dealer_score > player_score:
            break

    if player_score > 21:
        # Busted Player, dealer wins
        result_text.set("Dealer Wins!!")
        dealer_button.configure(state="disabled")
        dealer_wins.set(dealer_wins.get() + 1)
    elif dealer_score > 21 or dealer_score < player_score:
        # Either dealer is busted, or his score is less than player's
        result_text.set("Player Wins!!")
        dealer_button.configure(state="disabled")
        player_wins.set(player_wins.get() + 1)
    elif dealer_score > player_score:
        # If dealer score is greater than the player
        result_text.set("Dealer Wins!!")
        dealer_button.configure(state="disabled")
        dealer_wins.set(dealer_wins.get() + 1)
    else:
        # Last condition, same score
        result_text.set("Draw!!")
        dealer_button.configure(state="disabled")


def deal_player():
    # First go through deal_player_old() method..
    # also when doing so, uncomment player_score and player_ace global variables
    # That is the second way we ran this function
    player_hand.append(deal_cards(player_card_frame, deck))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)

    if player_score > 21:
        result_text.set("Dealer Wins!!")
        dealer_button.configure(state="disabled")
        player_button.configure(state="disabled")
        dealer_wins.set(dealer_wins.get() + 1)


# def deal_player_old():
#     # As long as we use a Global Variable in a function for reading purposes, Python is cool with that
#     # But as soon as we decide to assign values, it becomes agitated.. though here intellij just raises a warning
#     # Error comes to those, who try to read and write a global variable at same time...
#     # This is mainly because, Python considers a variable binded in a function a local variable, and it is trying to read the same variable before that thinking it as a global variable
#     # something like this.. instead of writing player_score = 0... we wrote player_score = player_score + 100
#     # Here, we are thinking to read global player_score... even while we are creating the local player_score at the same time
#     # In fact, if we try reading global player_score was read 2 lines earlier.. and then create a local player_score
#     # THAT WILL ALSO CAUSE ERROR... SAME PYTHON TO US... "MAKE UP YOUR MIND... I AM NOT A MIND READER"
#     # Function be like .... "Make up your mind... dude... Bang ERROR"
#     # At the end of the day, try not to use Global Variables this way
#
#     # So this is how we can use GLOBAL VARIABLE IN A FUNCTION as writable variable
#     # This is called SIDE-EFFECT...NAME SAYS IT ALL... TRY AVOIDING THIS.. OH!! BUT WHY?
#     # I don't know... ask 5 other functions WHO ARE ALSO DOING A LITTLE BIT OF GLOBAL MAGIC...;|
#     global player_ace, player_score
#     card_value = deal_cards(player_card_frame, deck)[0]
#     if card_value == 1 and not player_ace:
#         # Basically, if an ace is drawn, and player do not have an ace yet
#         card_value = 11
#         player_ace = True
#     player_score += card_value
#
#     if player_score > 21 and player_ace:
#         # if player busts, check if player has ace and deduce 10
#         player_score -= 10
#         player_ace = False
#
#     player_score_label.set(player_score)
#     if player_score > 21:
#         # Right now, we only are checking for this outcome, as dealer has not yet started working on his cards
#         result_text.set("Dealer Wins")
#
#     # To check all the local variables
#     # print(locals())

def prep_window():
    dealer_score_label.set(0)
    player_score_label.set(0)

    # This is the way to destroy only the children in a window
    for a_child in player_card_frame.winfo_children():
        a_child.destroy()

    for a_child in dealer_card_frame.winfo_children():
        a_child.destroy()

    dealer_hand.clear()
    player_hand.clear()
    result_text.set('')
    player_button.configure(state="normal")
    dealer_button.configure(state="normal")
    deck.clear()


def new_game():
    prep_window()

    # Here we are creating a copy of this list
    # Not sure why though - #TODO - Checkout if the reason mentioned is correct
    deck.extend(cards)
    # Now shuffling this deck
    random.shuffle(deck)
    print(len(deck))
    # So, first player is dealt a card
    deal_player()
    # Then dealer gets a card
    dealer_hand.append(deal_cards(dealer_card_frame, deck))
    dealer_score_label.set(score_hand(dealer_hand))
    # Then players gets another card
    deal_player()

    # return new_deck


main_window = tkinter.Tk()
main_window.geometry("640x480+600+200")
main_window.title("~=Black Jack=~")

# Changing main_window background to green
main_window['background'] = "green"

title_frame = tkinter.Frame(main_window)
title_frame.grid(row=0, column=0, sticky='we')

# This is to see the number of dealer wins
dealer_wins = tkinter.IntVar()
tkinter.Label(title_frame, text="Dealer:").grid(row=0, column=0, sticky='w')
dealer_wins_w = tkinter.Label(title_frame, textvariable=dealer_wins)
dealer_wins_w.grid(row=0, column=1, sticky='w')

# result_text will contain the result of the Game
result_text = tkinter.StringVar()
result = tkinter.Label(title_frame, textvariable=result_text)
result.grid(row=0, column=2, sticky='we')

# This is to see the number of player wins
player_wins = tkinter.IntVar()
tkinter.Label(title_frame, text="Player:").grid(row=0, column=3, sticky='w')
player_wins_w = tkinter.Label(title_frame, textvariable=player_wins)
player_wins_w.grid(row=0, column=4, sticky='w')

title_frame.columnconfigure(0, weight=1)
title_frame.columnconfigure(1, weight=1)
title_frame.columnconfigure(2, weight=1000)
title_frame.columnconfigure(3, weight=1)
title_frame.columnconfigure(4, weight=1)

# This is where Cards are going to be
card_frame = tkinter.Frame(main_window, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='we', columnspan=3, rowspan=2)

rules_frame = tkinter.Frame(main_window, relief="sunken", borderwidth=10, background="blue")
rules_frame.grid(row=4, column=0)
rules_data = tkinter.Text(rules_frame, background="lightblue", height=7)
rules_data.grid(row=0, column=0)
rules_data.insert(tkinter.END, "Rules:\n1. If you(player1) want another card - hit player button.\n"
                               "2. If you(player1) want to hold, hit dealer button.\n"
                               "3. If you(player1) hit dealer button... that means player is saying he is now on hold "
                               "and player button will be disabled.")

# This is setting up dealer score and label
dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# This is setting up frame for dealer cards
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky='we', rowspan=2)

# This is setting up player score and label
player_score_label = tkinter.IntVar()
# These are 2 global variables to help with calculating player score
# player_score = 0
# player_ace = False
# We do not need these after using new type of function... uncomment these when trying with deal_player_old()
tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# This is setting up frame for player cards
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='we', rowspan=2)

# Adding Button Frames from dealer and player
button_frame = tkinter.Frame(main_window)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

# Dealer Button
dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

# Player Button
player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

# New Game Button
new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game)
new_game_button.grid(row=0, column=2)

# Quit Button
quit_button = tkinter.Button(button_frame, text="Quit", command=main_window.destroy)
quit_button.grid(row=0, column=3)

# Calling load_cards in blackjack_loadcards module to load all the cards
cards = load_cards()
# Here we are creating a copy of this list
# Not sure why though - #TODO - Checkout if the reason mentioned is correct
deck = []
# Now shuffling this deck
# random.shuffle(deck)

# Creating  lists that will handle dealer's and Player's cards
dealer_hand = []
player_hand = []

new_game()

# Right now, if dealer picks out a card, the comparison starts to check who wins
# Remember!! dealer can not hold and thus can't check for winner until dealer reaches score of 17 or above
# How, it should happen is that dealer button should only be clicked once player want to stick

# # So, first player is dealt a card
# deal_player()
# # Then dealer gets a card
# dealer_hand.append(deal_cards(dealer_card_frame, deck))
# # Then players gets another card
# deal_player()
# Now, player can deal card(i.e. hit) or hold(no more cards for player)
# If player wants another card - hit player button
# If player wants to hold.. hit dealer button
# If player hits dealer button... that means player is saying he is now on hold and player button will disable
# Now go back to deal_dealer function... where we are going to keep on dealing card until score is >=17

main_window.update()
main_window.minsize(width=rules_frame.winfo_width(), height=title_frame.winfo_height() + card_frame.winfo_height() + button_frame.winfo_height() + rules_frame.winfo_height())
main_window.maxsize(width=rules_frame.winfo_width(), height=main_window.winfo_height())

main_window.mainloop()
