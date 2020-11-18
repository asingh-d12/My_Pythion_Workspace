data = [4, 5, 103, 104, 105, 110, 120, 130, 150, 160, 170, 183, 185, 188, 187, 191, 350, 360]

min_val = 100
max_val = 200

for i, val in enumerate(data):
    if val < min_val or val > max_val:
        del data[i]

print(data)
