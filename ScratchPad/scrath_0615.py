def a_func(*args, **kwargs):
    print(args)
    print(*args, sep=';')
    print(type(args))
    print('*' * 50)
    print(kwargs)
    print(*kwargs)
    # This won't work because, **kwargs basically means print(x=1, y=2).. which fails since print function doesn't have these keyword arguments
    # print(**kwargs)

total = 10
def a_func_2():
    global total
    total = total + 1
    print(total)

if __name__ == "__main__":
    a_func(1, 2, 3, 4, 5, x=1, y=2)
    print('*' * 50)
    a_func_2()
