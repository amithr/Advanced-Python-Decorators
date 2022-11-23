def outer_func(who):
    def inner_func():
        print(f"Hello, {who}")
    # This line is part of the outer function        
    inner_func()

outer_func("World!")

