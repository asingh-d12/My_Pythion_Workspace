# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.
import datetime
import pytz
import random


def random_the_timezones():
    # First let's randomize the list of timezones that user can select from
    random_timezones = []
    while len(random_timezones) < 9:
        select_this = random.randint(0, len(pytz.all_timezones) - 1)
        random_timezones.append(pytz.all_timezones[select_this])
    return random_timezones


# Now, we have created our random list of timezone selection, let's ask user
# to select 1
while True:
    random_timezones = random_the_timezones()
    print("Select 1 of these options, and see the time in the timezone with "
          "UTC time(0 to exit)")
    for index, a_timezone in enumerate(random_timezones):
        print("\t{} -> {}".format(index + 1, a_timezone))
    the_input = int(input("Enter your choice : "))
    if the_input == 0:
        break

    utc_time = pytz.utc.localize(datetime.datetime.utcnow())
    print("UTC time = {} {}".format(utc_time, utc_time.tzinfo))

    local_time = utc_time.astimezone(pytz.timezone(
        random_timezones[the_input - 1]))

    print("Local time of {} = {} {}".format(random_timezones[the_input - 1],
                                            local_time,
                                            local_time.tzname()))
