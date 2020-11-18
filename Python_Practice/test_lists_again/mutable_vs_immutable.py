# Mutables are call by reference
# Immutables are call by value


def func(my_data):
    if isinstance(my_data, list):
        my_data.append(100)
        print("List in my_func = {}".format(my_data))

    if isinstance(my_data, str):
        my_data += " from my_func"
        print("String in my_func = {}".format(my_data))


if __name__ == '__main__':
    data_list = [1, 2, 3, 4, 5]
    func(data_list)
    print(data_list)

    data_str = "Amrit"
    func(data_str)
    print(data_str)
