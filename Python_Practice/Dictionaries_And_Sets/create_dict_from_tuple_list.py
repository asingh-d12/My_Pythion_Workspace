# Here we will have a tuple or list with (key, value) pair as items.
# Let's create a list from it
fruit_tuple = (('orange', 'a sweet, orange, citrus fruit'), ('apple', 'round and crunchy'), ('grape', 'a small, sweet fruit growing in bunches'), ('lime', 'great with tequila'), ('pear', 'an oddly shaped apple'))
print(fruit_tuple)
dict_fruit_tuple = dict(fruit_tuple)
print(dict_fruit_tuple)

print("*" * 100)

fruit_tuple_list = [('orange', 'a sweet, orange, citrus fruit'), ('apple', 'round and crunchy'), ('grape', 'a small, sweet fruit growing in bunches'), ('lime', 'great with tequila'), ('pear', 'an oddly shaped apple')]
print(fruit_tuple_list)
dict_fruit_tuple_list = dict(fruit_tuple_list)
print(dict_fruit_tuple_list)

print("*" * 100)

fruit_list_list = [['orange', 'a sweet, orange, citrus fruit'],
                   ['apple', 'round and crunchy'],
                   ['grape', 'a small, sweet fruit growing in bunches'],
                   ['lime', 'great with tequila'],
                   ['pear', 'an oddly shaped apple']
                   ]
print(fruit_list_list)
dict_fruit_list_list = dict(fruit_list_list)
print(dict_fruit_list_list)

print("*" * 100)

fruit_list_tuple = (['orange', 'a sweet, orange, citrus fruit'],
                    ['apple', 'round and crunchy'],
                    ['grape', 'a small, sweet fruit growing in bunches'],
                    ['lime', 'great with tequila'],
                    ['pear', 'an oddly shaped apple']
                    )
print(fruit_list_tuple)
dict_fruit_list_tuple = dict(fruit_list_tuple)
print(dict_fruit_list_tuple)

# Though all of these work, it is recommended that (key, value) pairs are in tuple
