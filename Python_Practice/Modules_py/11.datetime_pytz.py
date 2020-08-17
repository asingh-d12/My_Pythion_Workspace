import pytz
import datetime

country = "Europe/Moscow"
# This methood provides me a datetime.tzinfo object, that then I can pass as
# argument to datetime.datetime functions
tz_to_disp = pytz.timezone(country)
# Now this is aware datetime object
local_time_in_country = datetime.datetime.now(tz=tz_to_disp)

print("Time in {} is {}".format(country, local_time_in_country))
# This UTC time is still Naive
print("UTC time = {}".format(datetime.datetime.utcnow()))

print("*" * 100)

# Though there is 1 thing, how do we know what String is required for any
# particular timezone.

# So, pytz module has a variable that is the list of all timezones.
for x in pytz.all_timezones:
    print(x, end="; ")

print("*" * 100)

# Not only this, but pytz also provides a dictionary with country names as
# key and timezone string as value.
for x in sorted(pytz.country_names):
    print("{} -> {}".format(x, pytz.country_names[x]),  end="; ")

print("*" * 100)
# Now, we have 2 things above
# 1. all timezones
# 2. all countries that are related to this country code
# 3. Now, what if we want to retrieve timezones corresponding to a country
# There is a dict for that as well in pytz... pytz.country_timezones
# in pytz.country_timezones.. key is the country code amd value are the
# timezones
# for x in sorted(pytz.country_names):
#     print("{} -> {}".format(x, pytz.country_timezones[x]), end='; ')

# There is 1 issue in running this like this, because the keys is
# pytz.country_names are all countries, but all the countries do not have
# timezones. For ex: Bouvet Island

print("*" * 100)
# We are going to access all the timezones present in a country, but we need
# to be defensive in case any country don't have a timezone.
# Instead of directly access, let's use get in case of country_timezones dict
for x in pytz.country_names:
    print("{} -> {} -> {}".format(x, pytz.country_names[x],
                                  pytz.country_timezones.get(x)))

# Awesome, NO Error now.
