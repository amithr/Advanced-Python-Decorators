import time

def timer(function):
    """Print the runtime of the decorated function"""
    def wrapper_timer(*args):
        start_time = time.perf_counter()    # 1
        value = function(*args)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

# Execute wrapper_timer
waste_some_time(5)

def slow_down(function):
    """Sleep 1 second before calling the function"""
    def wrapper_slow_down(*args):
        time.sleep(1)
        return function(*args)
    return wrapper_slow_down

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)