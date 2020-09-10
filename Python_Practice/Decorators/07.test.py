def a_upper_func():
    def a_func(func):
        print("This is before I execute the func")
        return func
    return a_func


@a_upper_func()
def a_dec_func():
    print("hello")


a_dec_func()
