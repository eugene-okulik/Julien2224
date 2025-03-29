def repeat_me(count):
    def decorator(func):
        def wrapper(*args):
            for i in range(count):
                func(*args)
        return wrapper
    return decorator


@repeat_me(count=7)
def example(text):
    print(text)


example('print_me')
