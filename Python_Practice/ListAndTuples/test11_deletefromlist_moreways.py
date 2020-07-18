# So earlier we noticed if we try removing items from the list while iterating over it,
# it can cause issues.

# and for we used some ways to overcome that

# Though will the issues still remain if we iterate backwards
a_list = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160,
          170, 183, 185, 187, 188, 191, 350, 360]

min_val = 100
max_val = 200

# print(range(1, 100)[0:10:2])

# Remember enumerate is not a sequence type... thus not subsriptable directly
for i, an_item in list(enumerate(a_list))[::-1]:
    if not min_val < an_item < max_val:
        del a_list[i]

print(a_list)

# So, a sorted list works great with traversing back method...
# Why does traversing back method work?
# Simple,
# Because whether item is set to delete or now... the pointer will always shift left
# and if item is deleted... whatever is shifting to left is already been traversed.. so no negative effects

print("*" * 100)

# Let's try the same method with unsorted list... it should work
a_list = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]
for i, an_item in list(enumerate(a_list))[::-1]:
    if not min_val < an_item < max_val:
        del a_list[i]

print(a_list)

print("*" * 100)
# Let's check out another way to delete from list
# this one using method reversed
# We are not explicitly converting enumerate object to list here
# But that has a disadvantage
a_list = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]
org_len = len(a_list)
for index, item in enumerate(reversed(a_list)):
    # Yep, that's the disadvantage... it will give 0 index to last item
    # print(index, item)
    # But we can go pass that with manipulating the index itself
    index = org_len - index - 1
    # Next, Logic to delete
    if not min_val < item < max_val:
        print(index, item)
        del a_list[index]

print(a_list)
