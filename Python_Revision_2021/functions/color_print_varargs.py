# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def colour_print(text: str, *effects: str) -> None:
    """
    This will provide effects to the text printed in the terminal window.

    :param text: Text that you want to print
    :param effects: add 0 or more effects to see text with various effects
    :return: None
    """
    output_str = "{}{}{}".format("".join(effects), text, RESET)
    print(output_str)


if __name__ == '__main__':
    colour_print("Hello, Red", RED)
    colour_print("Hello, Red", RED, BOLD)
    colour_print("Hello, Red", RED, BOLD, UNDERLINE)
    # # test that the colour was reset
    colour_print("This should be in the default terminal colour")
    colour_print("Hello, Blue", BLUE, REVERSE)
    colour_print("Hello, Blue", BLUE, REVERSE, UNDERLINE)
    colour_print("Hello, Yellow", YELLOW)
    colour_print("Hello, Bold", BOLD)
    colour_print("Hello, Underline", UNDERLINE)
    colour_print("Hello, Reverse", REVERSE)
    colour_print("Hello, Black", BLACK)