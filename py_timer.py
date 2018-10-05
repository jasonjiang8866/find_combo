import functools, time

def py_timer(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        starting=time.time()
        value = func(*args, **kwargs)
        duration=time.time()-starting
        return value,duration
    return wrapper_decorator
