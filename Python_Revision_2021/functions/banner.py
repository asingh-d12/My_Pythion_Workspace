def print_banner(the_string, max_space=80):
    """

    This will print a String formatted in center.

    :param the_string: The String user wants to see centered.
    :param max_space: `int` representing the width in which the string is centered.
    :return: None
    :raise ValueError:  if the supplied string's length is greater than max width
    """
    if len(the_string) > max_space - 4:
        raise ValueError("String {} is larger than specified width".format(the_string, max_space))
    if the_string == "*":
        print("*" * max_space)
    else:
        the_string_to_print = "{0}{1}{0}".format("*" * 2, the_string.center(max_space - 4))
        print(the_string_to_print)


if __name__ == '__main__':
    print_banner("*")
    print_banner("Hello World")
    print_banner("My name is Amrit!!")
    print_banner("I am a Performance Engineer.")
    print_banner("*")
    # print(dir(print_banner))
