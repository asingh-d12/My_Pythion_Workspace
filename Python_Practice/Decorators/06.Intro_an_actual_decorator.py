def new_decorator(func):
    print("Welcome to new decorator!!")

    def wrap_func():
        print("Some code before executing func")
        func()
        print("Some code after executing func")

    return wrap_func


# Instead of doing all the things we did in these 2 lines
# a_func_needs_decorate = new_decorator(a_func_needs_decorate)
# a_func_needs_decorate()
# We can simply add this to say this function is being wrapped
@new_decorator
def a_func_needs_decorate():
    print("This is inside func needing decorating!!")


# Now that we have decorated the function... just directly call the function
a_func_needs_decorate()




# # Calling this directly, with no changes or additions made
# a_func_needs_decorate()
# # Output --> "This is inside func needing decorating!!"
#
# print("*" * 100)
#
# # What if i do this now.. what will be the output?
# a_func_needs_decorate = new_decorator(a_func_needs_decorate)
# a_func_needs_decorate()
# # The output is-->
# # Welcome to new decorator!!
# # Some code before executing func
# # This is inside func needing decorating!!
# # Some code after executing func
#
# # This is what exactly the decorator does...
# # It takes a function which needs more functionality...adds the functionality
# # above or below or both side of the function and then function executes in
# # the middle
# # So basically... IT WRAPS THE FUNCTION IN ITSELF
