import shelve

with shelve.open("bike_2") as bike:
    bike["make"] = "Honda"
    bike['model'] = "CBR1000"
    bike["color"] = "Blue"
    # Create wrong key by mistake
    bike['engin_size'] = 1000

    print("*" * 50)

    for a_key in bike:
        print("{} -> {}".format(a_key, bike[a_key]))

    # delete the wrong key
    del bike['engin_size']

    print("*" * 50)

    for a_key in bike:
        print("{} -> {}".format(a_key, bike[a_key]))

    print("*" * 50)

    bike['engine_size'] = 1000

    for a_key in bike:
        print("{} -> {}".format(a_key, bike[a_key]))
