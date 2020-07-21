# We can do something like this, when we are writing code:
x = y = z = 132
# Basically binding same value to 3 variables
print(x)
print(y)
print(z)

print('*' * 50)

# We can also do this
x, y, z = 1500, 345, 22
# This is unpacking a tuple
print(x)
print(y)
print(z)

print('*' * 50)

# Let's create a tuple
a_tuple = "Amrit", 30, "M"
name, age, gender = a_tuple
# This is also UNPACKING TUPLE
print(name)
print(age)
print(gender)

print('*' * 50)

# Unpacking a List is also possible
names = ["Amrit", "Lucky", "Ravi"]
n1, n2, n3 = names
print(n1)
print(n2)
print(n3)
names[1] = "Jupnit"
print(names)
# I think n2 will still be Lucky
print(n2)

print("*" * 100)

# One issue with unpacking lists
a_list = ["Amrit", "Lucky", "Ravi"]
# Some days later i am adding this code
a_list.remove("Lucky")
# Will the line below work now?
n1, n2, n3 = a_list
print(n1)
print(n2)
print(n3)
# This error will come even if we add more items

