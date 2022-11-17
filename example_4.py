# When using a decorator parameter, you need to have an inner
# decorator function in addition to the external decorator function
# The actual_decorator_func is the one that actually executes
# and adds additional functionality
def decorator(*args, **kwargs):
    print("Inside decorator")
    def inner_decorator(function):
        def actual_decorator_func():
            # code functionality here
            print("Inside inner function")
            print("I like", kwargs['name'])
            function()
        return actual_decorator_func
         
    # returning inner function   
    return inner_decorator
 
@decorator(name = "John")
def my_func():
    print("Inside actual function")

# This executes the inner actual_decorator_func
my_func()