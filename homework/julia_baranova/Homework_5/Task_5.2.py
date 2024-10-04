text1 = 'результат операции: 42'
text2 = 'результат операции: 514'
text3 = 'результат работы программы: 9'

number1_index = text1.index('42')
number2_index = text2.index('514')
number3_index = text3.index('9')
print(int(text1[number1_index:]) + 10)
print(int(text2[number2_index:]) + 10)
print(int(text3[number3_index:]) + 10)
