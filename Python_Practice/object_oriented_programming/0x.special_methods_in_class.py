# So we know how we are able to run functions like len(), print() etc for
# virtually any type of object... how is it actually possible.

# to understand check this class out

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # How to make sure that when i print(<book object>).. it is something
    # more than just the type of object and location

    # Here comes the answer
    # We can override this special method inside of our class and make sure
    # that print prints something useful
    # There are 2 methods we can override
    # 1. __str__()
    # 2. __repr__() --> we will override this, as this is more common in Flask

    def __repr__(self):
        # Now, whatever we want to get printed, let's return it
        return "Title -> {}\nAuthor -> {}\nNum of Pages -> {}".format(
            self.title, self.author, self.num_pages)

    # What is the special method to be implemented(not overridden) to run len()
    # function on our object
    def __len__(self):
        # Simply return number of pages in the book
        return self.num_pages


# Let's create an instance of the book class
my_book = Book("My Journey", "Shiman Dev", 200)

print(my_book)
# Right now, i can only see this output
# <__main__.Book object at 0x7f4885b91820>
# Basically telling me that this is a book object at this location

# Now i run after overriding __repr__() method

print("Length after implementing __len__() method = {}".format(len(my_book)))
