def operation(func):
    def wrapper(f, s):
        if f < 0 or s < 0:
            op = '*'
        elif f == s:
            op = '+'
        elif f > s:
            op = '-'
        else:
            op = '%'
            return func(f, s, op)
        return wrapper


@operation
def calc(f, s, op):
    if op == '+':
        return f + s
    elif op == '-':
        return f - s
    elif op == '%':
        return f / s
    elif op == '*':
        return f * s


numbers = input('Please write two numbers:')
first, second = map(int, numbers.split())

result = calc(first, second)
print(result)
