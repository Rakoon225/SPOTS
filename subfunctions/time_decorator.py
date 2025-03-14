import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} выполнена за {end_time - start_time:.6f} секунд.")
        return result
    return wrapper
