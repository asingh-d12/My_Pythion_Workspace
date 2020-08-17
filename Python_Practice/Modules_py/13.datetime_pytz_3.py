import datetime
import pytz

# So, what we want to understand is how to change local time to utc time
# First, let's create Naive local time
local_time = datetime.datetime.now()
# Now, let's create naive utc time
utc_time = datetime.datetime.utcnow()

print("Naive Local Time = {}".format(local_time))
print("Naive UTC Time = {}".format(utc_time))

# Now, let's convert Naive Local time to Aware Local time using a function
# pytz provides
# aware_local_time = pytz.utc.localize(local_time)
# We are commenting the above statement, and instead using this one
# astimezone() is a method to convert aware time to local timezone
# if no argument is provided... if argument is provided then convert to that

# NOTE:: If this method is called with naive datetime.. it will assume the time
# to be in local timezone

# Getting back to matter in hand.. convert utc time to any timezone
# right now it is converting to local timezone.
aware_local_time = pytz.utc.localize(utc_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)
print("Aware Local Time = {} {}".format(aware_local_time,
                                        aware_local_time.tzinfo))
# Only NAIVE UTC time is valid input for this pytz.utc.localize() function...
# otherwise, it will show local time as utc
# as well

print("Aware UTC Time = {} {}".format(aware_utc_time,
                                      aware_utc_time.tzinfo))

print("*" * 100)
local_moscow_time = datetime.datetime.now(tz=pytz.timezone('Europe/Moscow'))
print(local_moscow_time)
# How to convert this back to UTC time
utc_time = local_moscow_time.astimezone(pytz.utc)
print(utc_time)
