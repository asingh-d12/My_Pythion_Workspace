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


while True:
    print("These are all the albums!!")
    for index, an_album in enumerate(albums):
        print("{} -> {}".format(index + 1, an_album[0]))

    ch = int(input("Enter the Album you want to play(incorrect choice will exit) : ")) - 1
    if ch < 0 or ch > len(albums) - 1:
        break
    else:
        print("All the songs in this album!!")
        for i, a_song in albums[ch][3]:
            print("{} -> {}".format(i, a_song))
        song_ch = int(input("Select the song you want to play!! : ")) - 1

        if 0 <= song_ch < len(albums[ch][3]):
            print("Playing -> {}".format(albums[ch][3][song_ch][1]))
        else:
            print("Incorrect song number!!")
    print("*" * 50)

