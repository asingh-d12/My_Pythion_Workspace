import shelve

# Here we are going to demonstrate that different type of information
# can be stored in a shelf

with shelve.open("bike") as bike:
    bike["make"] = "Honda"
    bike['model'] = "CBR1000"
    bike["color"] = "Blue"
    bike['engine_size'] = 1000

    # Now printing data
    print(bike["model"])
    print(bike['engine_size'])

    print("*" * 50)

    for a_key in bike:
        print("{} -> {}".format(a_key, bike[a_key]))
