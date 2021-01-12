def format_string(a_str, width=80):
    if len(a_str) > width - 4:
        raise ValueError("The String '{}' has length that is higher that the width of {}".format(a_str, width))

    if a_str == '*':
        print('*' * width)
    else:
        print("**{}**".format(a_str.center(width - 4)))


format_string('*')
format_string("Always look on the bright side of life...", 20)
format_string('*')
