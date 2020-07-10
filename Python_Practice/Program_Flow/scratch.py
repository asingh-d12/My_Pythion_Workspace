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

# Checking how simple split works
a_str = "a b c d"
print(a_str.split())

a_str = "a    \nb  c  d"
print(a_str.split())

a_str = "a b c \n\t   d"
print(a_str.split())

a_str = "a b   \t\nc d"
print(a_str.split())

a_str = "a    b c   d"
print(a_str.split())

print('*' * 100)

for i in range(20):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)

print("*" * 50)
number = 5
multiplier = 8
answer = 0

# add your loop after this comment
for _ in range(multiplier):
    answer += number

print(answer)
