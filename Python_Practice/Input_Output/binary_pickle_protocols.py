# Let's store more than 1 object

import pickle

# This is the tuple that we want to store
imelda = ('More Mayhem',
          'Imelda MAy',
          '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')
           )
          )

# Lists we want to store
even_list = list(range(0, 10, 2))
odd_list = list(range(1, 10, 2))

with open("imelda.pickle", "wb") as pickle_file:
    # Basically the whole nested tuple is stored in this 1 call
    pickle.dump(imelda, pickle_file, protocol=0)
    pickle.dump(even_list, pickle_file, protocol=1)
    pickle.dump(odd_list, pickle_file, protocol=3)
    pickle.dump(2998902, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump("By: Amrit Singh", pickle_file, protocol=pickle.DEFAULT_PROTOCOL)

# Let's read the pickle
# 1 object at a time
with open("imelda.pickle", 'rb') as pickle_file_2:
    imelda_tuple = pickle.load(pickle_file_2)
    print(imelda_tuple)
    even_list_loaded = pickle.load(pickle_file_2)
    print(even_list_loaded)
    odd_list_loaded = pickle.load(pickle_file_2)
    print(odd_list_loaded)
    num_loaded = pickle.load(pickle_file_2)
    print(num_loaded)
    by_str_loaded = pickle.load(pickle_file_2)
    print(by_str_loaded)

# Awesome, everything is loaded 1 by 1
# Just, make sure that the order you dumped in should be same as order you
# read in

print(pickle.DEFAULT_PROTOCOL)
