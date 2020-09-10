import random
import tkinter


def load_cards() -> list:
    card_images = []
    suits = ["heart", "club", "diamond", "spade"]
    face_cards = ["jack", "queen", "king"]

    for suit in suits:
        # First going through number cards
        for card_num in range(1, 11):
            name = 'cards/{}_{}.png'.format(card_num, suit)
            # This is how an image is read in Tkinter
            image = tkinter.PhotoImage(file=name)
            card_images.append((card_num, image))

        # Now for face cards
        for a_face in face_cards:
            name = 'cards/{}_{}.png'.format(a_face, suit)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))

    # returning after shuffling
    return card_images


def deal_cards(frame, deck):
    # Pop the next card of the top of the deck
    # If all 52 cards are popped, we will start getting errors
    # but we can ignore that error, since that situation should never arise as 21 count will be reached way earlier
    next_card = deck.pop(0)

    # Even though our main_window is grid, we can use pack manager in a child window
    # Though make sure we don't have grid and pack manager in the same window
    # This is how we are adding images
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')

    # now return card face value
    return next_card


def score_hand(hand) -> int:
    """The purpose of this function is to calculate the total score of the hand
    Only 1 ace can have value of 11... so keep that in mind
    :returns: total score"""
    score = 0
    ace = False

    for next_card in hand:
        card_value = next_card[0]

        if card_value == 1 and not ace:
            card_value = 11
            ace = True

        score += card_value

        if card_value > 21 and ace:
            card_value -= 10
            ace = False

    return score
