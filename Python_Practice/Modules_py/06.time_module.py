import time

# Basically time since epoch.. as it is 0, it gives epoch start as output
# gmtime returns time in a named tuple, argument being the seconds since epoch
print(time.gmtime(0))
# If nothing is mentioned in argument, it gives current gmtime
print(time.gmtime())

# This gives current localtime in a named tuple.
# we can give argument, if we want to specify how many seconds since epoch
# started
print(time.localtime())

# This gives current epoch time in seconds
print(time.time())

# Since gmtime and localtime are returning a named tuple, we can also do
# something like this.
time_local = time.localtime()
print("Local Year = {}".format(time_local.tm_year))
print("Local Month = {}".format(time_local.tm_mon))
print("Local Day of Month = {}".format(time_local.tm_mday))
print("Local Hour = {}".format(time_local.tm_hour))
print("Local Min = {}".format(time_local.tm_min))
print("Local Second = {}".format(time_local.tm_sec))
