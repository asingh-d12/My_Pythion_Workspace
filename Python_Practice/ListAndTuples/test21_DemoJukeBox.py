# We are importing all the data in albums from previous python file
from test20_albumtuplesintuples import albums

# Any variable name in ALL CAPITALS is a constant
SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please choose an album, invalid choice kills the program.")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{} -> {}".format(index + 1, title))

    choice = int(input("Please enter your choice : "))
    if not 0 < choice <= len(albums):
        break

    album_chosen = albums[choice - 1]
    print("Please select the song you want to play, invalid choice bring back to Albums.")
    for index, song in album_chosen[SONGS_LIST_INDEX]:
        print("{} -> {}".format(index, song))

    choice = int(input("Please enter your choice : "))

    if not 0 < choice <= len(album_chosen[SONGS_LIST_INDEX]):
        continue
    index_choose = choice - 1

    print("Playing song {}".format(album_chosen[SONGS_LIST_INDEX][index_choose][SONG_TITLE_INDEX]))
    print("*" * 50)

