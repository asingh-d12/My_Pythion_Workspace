import datetime

# Return the current local datetime, but is naive
print(datetime.datetime.today())

# This prints the time at this moment, and even though object is Naive it
# shows system time
print(datetime.datetime.now())

# today() and now() are similar except for tz parameter that can be provided
# in now() method. now() method is more precise

# This prints the time at this moment, and even though object is Naive it
# shows UTC time
print(datetime.datetime.utcnow())
