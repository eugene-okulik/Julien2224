text1 = 'результат операции: 42'
text2 = 'результат операции: 514'
text3 = 'результат работы программы: 9'

number1 = int(text1[text1.index(':') + 1:].strip())
number2 = int(text2[text2.index(':') + 1:].strip())
number3 = int(text3[text3.index(':') + 1:].strip())

print(number1 + 10)
print(number2 + 10)
print(number3 + 10)
