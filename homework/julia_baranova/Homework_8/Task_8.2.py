import sys
sys.set_int_max_str_digits(100000)


def fibonacci_generator():
    a, b = 0, 1
    index = 0
    while True:
        yield index, a
        a, b = b, a + b
        index += 1


def get_fibonacci_by_index(n):
    gen = fibonacci_generator()
    for index, number in gen:
        if index == n:
            return number


print(get_fibonacci_by_index(4))
print(get_fibonacci_by_index(199))
print(get_fibonacci_by_index(999))
print(get_fibonacci_by_index(99999))
