welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

# So, we have these 5 tuples, each representing an album
# What if we want these albums to be in a single list
albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984)
          ]

# Now albums is a list containing all the albums, each album being a tuple
# Now we can traverse through all these albums
for an_album in albums:
    album_name, artist, yr = an_album
    print("{} - {} - {}".format(album_name, artist, yr))
