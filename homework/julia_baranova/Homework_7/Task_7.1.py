number1 = 5
while True:
    number2 = int(input('Угадай цифру'))
    if number1 != number2:
        print('попробуйте снова')
    else:
        print('Поздравляю! Вы угадали!')
        break
