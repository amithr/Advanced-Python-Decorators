def decorator(*args, **kwargs):
    print("Inside decorator")
    def inner(function):
         
        # code functionality here
        print("Inside inner function")
        print("I like", kwargs['name'])
         
        function()
         
    # returning inner function   
    return inner
 
@decorator(name = "John")
def my_func():
    print("Inside actual function")