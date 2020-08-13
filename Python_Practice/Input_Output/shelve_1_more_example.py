import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

books = {"recipes": {"blt": blt,
                     "beans_on_toast": beans_on_toast,
                     "scrambled_eggs": scrambled_eggs,
                     "soup": soup,
                     "pasta": pasta
                     },
         "maintanence": {"stuck": ["oil"],
                         "loose": ["gaffer tape"]
                         }
         }

print(books["recipes"]["soup"])
print(books["recipes"]["scrambled_eggs"])

print(books["maintanence"]["loose"])

print("*" * 100)

# To change the above mentioned dictionary to shelve, we have to make a
# couple of changes
shelve_books = shelve.open("books.shelve")
shelve_books["recipes"] = {"blt": blt,
                           "beans_on_toast": beans_on_toast,
                           "scrambled_eggs": scrambled_eggs,
                           "soup": soup,
                           "pasta": pasta
                           }
shelve_books["maintanence"] = {"stuck": ["oil"],
                               "loose": ["gaffer tape"]
                               }

print(shelve_books["recipes"]["soup"])
print(shelve_books["maintanence"]["stuck"])

shelve_books.close()
