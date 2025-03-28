def operation_chooser(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        else:
            operation = '%'
        return func(first, second, operation)
    return wrapper


@operation_chooser
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '%':
        return first / second
    elif operation == '*':
        return first * second


numbers = input('Please write two numbers:')
first, second = map(int, numbers.split())

result = calc(first, second)
print(result)
