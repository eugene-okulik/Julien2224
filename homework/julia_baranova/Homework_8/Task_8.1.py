import random

salary = int(input('What is your salary?'))
bonus = random.choice([True, False])
big_salary = 0

if bonus:
    big_salary = salary + random.randint(10, 100000)
else:
    big_salary = salary

print(f"{salary}, {bonus} - '${big_salary}'")
