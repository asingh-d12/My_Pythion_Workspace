a_set = {3, 1, 5, 1, 2, 5, 6, 7, 4, 3}
print(sorted(a_set))

a_tuple = (1, 3, 1, 4, 3, 2, 6, 87, 12, 34, 56, 12, 1)
print(sorted(a_tuple))

a_list = [3, 4, 1, 5, 12, 51, 12, 34, 53, 123, 12]
print(sorted(a_list))

print('*' * 100)

a_list = [3, 4, 1, 5, 12, 51, 12, 34, 53, 123, 12]
print("Listed from sorted() function = {}".format(sorted(a_list)))
print("Original list after sorted() = {}".format(a_list))
print("What is returned when .sort() method is used = {}".format(a_list.sort()))
print("Original list after .sort() method = {}".format(a_list))

print("*" * 100)
# Case Insensitive Sorting
pangram = "The quick brown fox jumps over the lazy dog"
print(pangram)
print(sorted(pangram))
print(sorted(pangram, key=str.casefold))
