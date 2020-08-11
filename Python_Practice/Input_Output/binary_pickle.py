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

with open("imelda.pickle", "wb") as pickle_file:
    # Basically the whole nested tuple is stored in this 1 call
    pickle.dump(imelda, pickle_file)

# PICKLE ONLY CAN BE READ IN PYTHON

# Let's read back the nested tuple
with open("imelda.pickle", 'rb') as pickle_file_2:
    imelda_tuple = pickle.load(pickle_file_2)
    print(imelda_tuple)
