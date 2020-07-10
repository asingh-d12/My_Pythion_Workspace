import random

# First let's create some random List
a_list = list(range(1, 1001))


# This is a random list generator, which is actually something not used in Binary Search.. because List is to be sorted
# first
def random_list_gen():
    num_of_runs = 0

    while True:
        to_add = random.randint(1, 100)
        num_of_runs += 1
        print("Number to add = {}".format(to_add))
        if to_add in a_list:
            print("Number {} already present, skipping this number".format(to_add))
            continue
        a_list.append(to_add)
        print("{} added".format(to_add))
        if len(a_list) == 100:
            break

    print(a_list)
    print("Complete list created in {} runs of while loop".format(num_of_runs))


print("*" * 100)


# Next Part is binary search algorithm
def b_s(start, end, to_search):
    global rec_level
    mid = (start + end) // 2
    rec_level += 1
    if to_search == a_list[mid]:
        print("You have searched the number {} at position".format(mid))
        return
    elif to_search > a_list[mid]:
        start = mid + 1
        b_s(start, end, to_search)
    else:
        end = mid - 1
        b_s(start, end, to_search)


def main():
    global rec_level
    to_search_l = random.randint(1, 1001)
    print("I am going to search number = {}".format(to_search_l))
    start_l = 0
    end_l = len(a_list) - 1
    b_s(start_l, end_l, to_search_l)
    print("Searched in {} times".format(rec_level))


if __name__ == '__main__':
    for i in range(5):
        rec_level = 0
        main()
