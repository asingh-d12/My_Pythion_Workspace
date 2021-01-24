albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

print("Welcome to the Juke Box!!")

ALBUM_NAME_INDEX = 0
SONGS_INDEX = 3
SONG_NAME_INDEX = 1
while True:
    print("Please choose the album you want to play(Invalid choice to quit)==>")
    for index, album in enumerate(albums):
        print("{}: {}".format(index + 1, album[ALBUM_NAME_INDEX]))

    ch = int(input("What is your choice: ")) - 1

    if not 0 <= ch < len(albums):
        print("Incorrect Choice, Bye Bye now!!")
        break

    # Here the part begins if choice is valid
    print("Select the song to play!!")
    for song_num, song_name in albums[ch][SONGS_INDEX]:
        print("{}: {}".format(song_num, song_name))

    song_choice = int(input("Please enter the choice: "))

    if not 1 <= song_choice <= len(albums[ch][SONGS_INDEX]):
        print("Incorrect Choice, Try again!!")
    else:
        print("Playing song {}".format(albums[ch][SONGS_INDEX][song_choice - 1][SONG_NAME_INDEX]))

    print("=" * 50)
