# 1
def my_decorator(func):
    def wrapper():
        print("Message before function.")
        func()
        print("Message after function.")

    # This line is part of the outer function    
    return wrapper

def say_hello():
    print("Hello!")

say_whee = my_decorator(say_hello)

# 2
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

@do_twice
def say_good_bye():
    print("Good Bye!")

# This executes the inner, wrapper_do_twice function
say_good_bye()