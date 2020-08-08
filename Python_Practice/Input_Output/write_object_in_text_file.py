imelda = 'More Mayhem', 'Imelda MAy', '2011', \
         ((1, 'Pulling the Rug'),
          (2, 'Psycho'),
          (3, 'Mayhem'),
          (4, 'Kentish Town Waltz')
          )

print(imelda)
# So, now we have a tuple, let's write it to a file

with open("./imelda.txt", 'w') as imelda_file:
    # This will print tuple as a string in imelda.txt file
    print(imelda, file=imelda_file)
