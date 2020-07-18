import timeit

max_value = 1000000  # 100000000
min_valid = 10
max_valid = 999997  # 99999997

data_list1 = list(range(max_value))
data_list2 = list(range(max_value))
data_list3 = list(range(max_value))
data_list4 = list(range(max_value))


def sanitise_1(data):
    # This is very simple way... but can only be used for SORTED LISTS
    # process the low values in the list
    stop = 0
    for index, value in enumerate(data):
        if value >= min_valid:
            stop = index
            break

    del data[:stop]

    start = 0
    for index in range(len(data) - 1, -1, -1):
        if data[index] <= max_valid:
            # We have the index of last item to keep.
            # Set 'start' to the position of the first
            # item to delete, which is 1 after 'index'.
            start = index + 1
            break

    del data[start:]


def sanitise_2(data):
    top_index = len(data) - 1
    for index, value in enumerate(reversed(data)):
        if value < min_valid or value > max_valid:
            del data[top_index - index]


# def sanitise_3(data):
#     # Not going to use reversed here... using slices to reverse and explicit conversion
#     # It seems like this is not a good way ... the timing is higher
#     for index, value in list(enumerate(data))[::-1]:
#         if value < min_valid or value > max_valid:
#             del data[index]


def sanitise_4(data):
    for index in range(len(data) - 1, -1, -1):
        if data[index] < min_valid or data[index] > max_valid:
            del data[index]


def sanitise_3(data):
    i = 0
    while i < len(data):
        if data[i] < min_valid or data[i] > max_valid:
            del data[i]
            i -= 1
        i += 1


if __name__ == "__main__":
    print("Timing")
    x = timeit.timeit("sanitise_1(data_list1)",
                      setup="from __main__ import sanitise_1,"
                            "data_list1",
                      number=1)
    print("{:15.15f}".format(x))
    del data_list1
    y = timeit.timeit("sanitise_2(data_list2)",
                      setup="from __main__ import sanitise_2,"
                            "data_list2",
                      number=1)
    print("{:15.15f}".format(y))
    del data_list2
    z = timeit.timeit("sanitise_3(data_list3)",
                      setup="from __main__ import sanitise_3,"
                            "data_list3",
                      number=1)
    print("{:15.15f}".format(z))
    del data_list3
    n = timeit.timeit("sanitise_4(data_list4)",
                      setup="from __main__ import sanitise_4,"
                            "data_list4",
                      number=1)
    print("{:15.15f}".format(n))
    del data_list4

    # sanitise_1(data_list1)
    # print(data_list1)
    # sanitise_2(data_list2)
    # print(data_list2)
    # sanitise_3(data_list3)
    # print(data_list3)
    # sanitise_4(data_list4)
    # print(data_list4)
