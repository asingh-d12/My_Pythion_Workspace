def is_palindrome(a_str: str) -> bool:
    """

    :param a_str: A Word which is to be checked, if it is a palindome
    :return: bool
    """
    return a_str == a_str[::-1]


def is_palindrome_sentence(a_str: str) -> bool:
    """
    Checks if a sentence of type `str` is a Palindrome or not.

    :param a_str: Sentence of type string user will provide.
    :return: bool
    """
    final_str = ''.join([a_char for a_char in a_str if a_char.isalnum()])
    return is_palindrome(final_str)


a_string = input("Enter the String/sentence you want to check if it is Palindrome or not : ")
if " " not in a_string:
    print("Is this String Palindrome: {}".format(is_palindrome(a_string.casefold())))
    is_palindrome()
else:
    print("Is this Sentence Palindrome: {}".format(is_palindrome_sentence(a_string.casefold())))
