# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

some_text = "My name is Amritpal Singh Narula"
# vowel_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
vowel_set = frozenset("aeiouAEIOU")
some_text_set = set(some_text)
print(some_text_set)
no_vowel_some_text = sorted(some_text_set - vowel_set)
print(no_vowel_some_text)
