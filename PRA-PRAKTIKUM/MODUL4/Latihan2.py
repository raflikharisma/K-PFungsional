def uppercase_decorator(function):
    def wrapper():
        func = function()
        return func.upper()
    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there!'

# Single decorator
print(say_hi())
    