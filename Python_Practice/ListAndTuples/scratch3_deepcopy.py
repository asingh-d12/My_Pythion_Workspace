import copy

a_list = list(range(1, 10, 2))
b_list = [1, 2, 3, 4, a_list]
print(b_list)
c_list = b_list.copy()
print(c_list)

print(b_list[-1] is c_list[-1])

d_list = copy.deepcopy(b_list)
print(d_list)

print(b_list[-1] is d_list[-1])

# Odd way to copy list
print([*b_list])
