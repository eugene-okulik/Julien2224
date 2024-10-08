for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        number = 'FuzzBuzz'
    elif number % 3 == 0:
        number = 'Fuzz'
    elif number % 5 == 0:
        number = 'Buzz'
    print(number)
  