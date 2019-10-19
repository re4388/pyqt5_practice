import time

def log_calls(func):
    
    def wrapper(*args, **kwargs):
        now = time.time()
        print(f"Calling {func.__name__} with {args} and {kwargs}")

        return_value = func(*args, **kwargs)

        print(f"Executed {func.__name__} in {time.time() - now}ms")
        return return_value

    return wrapper