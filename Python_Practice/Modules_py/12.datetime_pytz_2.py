import datetime
import pytz

# Here I am going to print time for each and every timezone

for a_country in sorted(pytz.country_names):
    print("{} -> {}".format(a_country, pytz.country_names[a_country]))
    if a_country in pytz.country_timezones:
        for a_zone in sorted(pytz.country_timezones[a_country]):
            # So far everything is as was in previous file
            # This is where we are creating the timezone object
            tz_obj = pytz.timezone(a_zone)
            print("\t{} -> {}".format(a_zone, datetime.datetime.now(tz=tz_obj)))
    else:
        print("\tNo Timezone defined!!")
