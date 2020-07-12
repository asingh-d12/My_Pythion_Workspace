import random

random_list = []
max_l = 100
for i in range(max_l):
    random_list.append(random.randint(1, max_l))

print("PFB the list operations that can be done...")
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
print("min in even list = {}".format(min(even)))
print("max in even list = {}".format(max(even)))
print("min in odd list = {}".format(min(odd)))
print("max in odd list = {}".format(max(odd)))
print("*" * 50)
print("Length of even list = {}".format(len(even)))
print("Length of odd list = {}".format(len(odd)))

print("*" * 50)
print(random_list)
random_sorted_list = sorted(random_list)
i = 0
while i < max_l:
    print("{} -> {}".format(random_sorted_list[i], random_sorted_list.count(random_sorted_list[i])))
    # del random_sorted_list[:random_sorted_list.count(i)]
    i += random_sorted_list.count(random_sorted_list[i])

# print(random_list)
