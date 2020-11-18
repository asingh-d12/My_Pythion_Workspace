z = [1, 2, 3, 4, 5]
y = enumerate(z)

print(z)
for a, b in y:
    print(a, b)
    if b == 3:
        z.append(25)
