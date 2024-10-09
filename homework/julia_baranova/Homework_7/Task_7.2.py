words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def multtext(**kwargs):
    for key, value in kwargs.items():
        print(key * value)


multtext(**words)
