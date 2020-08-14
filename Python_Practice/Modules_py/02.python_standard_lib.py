print(dir())
# All the modules have __ at the start and end, that means Python does not
# want us to change this... this is in essence only for python
print("*" * 100)
# Now, let's get into __builtins__ which is the builtin module
print(dir(__builtins__))
