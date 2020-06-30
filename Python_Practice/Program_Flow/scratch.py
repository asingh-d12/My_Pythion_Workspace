# ints are always present in 1 single memory location no matter how you do the evaluation

# that's why int is immutable

i = 1
print(type(i))

x = 1
print(id(x))
print(id(i))

print(id(x) == id(i))

print('*' * 100)

i = 5
print(type(i))

x = i - 1 + 10 - 9
x = (10//i) + 3
print(id(x))
print(id(i))

print(id(x) == id(i))
