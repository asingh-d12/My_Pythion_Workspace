import time

print("Epoch on this system starts @ {}".format(time.strftime("%c",
                                                              time.gmtime(0))))

print("The current timezone is {} with an offset of {}".
      format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("Daylight saving time is in affect.")
    print("The DST timezone is {}".format(time.timezone[1]))
else:
    print("No Daylight saving time.")

print("Current Local time = {}".format(time.strftime("%Y-%m-%d %H:%M:%S",
                                                     time.localtime())))

print("Current UTC time = {}".format(time.strftime("%Y-%m-%d %H:%M:%S",
                                                   time.gmtime())))
