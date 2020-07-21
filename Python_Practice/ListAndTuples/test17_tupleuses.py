welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

# We have 5 tuples above, let's print 1
print(metallica)
# Tuples are subscriptable
print(metallica[0])
print(metallica[1])
print(metallica[2])

# Tuples are IMMUTABLE
# Let's check out
# metallica[0] = "Singles Day"
# If we try the statement above we get the following error
# TypeError: 'tuple' object does not support item assignment

# How to alter an item in tuple
# WE CAN'T
# Though we can do this
metallica_2 = list(metallica)
# Now we got a list, let's change the item in this list
metallica_2[0] = "A singles day"
print(metallica_2)
