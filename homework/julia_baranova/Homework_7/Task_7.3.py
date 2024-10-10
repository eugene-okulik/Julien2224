text1 = 'результат операции: 42'
text2 = 'результат операции: 514'
text3 = 'результат работы программы: 9'
text4 = 'результат: 2'


def number_in_text(*args):
    for text in args:
        number = int(text.split()[-1]) + 10
        print(number)


number_in_text(text1, text2, text3, text4)
