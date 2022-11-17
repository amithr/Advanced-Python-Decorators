def my_decorator(func):
    def wrapper():
        print("Message before function.")
        func()
        print("Message after function.")
    return wrapper

def say_hello():
    print("Hello!")

say_whee = my_decorator(say_hello)


def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

@do_twice
def say_good_bye():
    print("Good Bye!")

say_good_bye()