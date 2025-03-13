temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32,
                34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
temperatures_high = filter(lambda x: x > 28, temperatures)
temperatures_high = list(temperatures_high)
average_high_temp = sum(temperatures_high)/len(temperatures_high)
print(temperatures_high)
print(max(temperatures_high))
print(min(temperatures_high))
print(round(average_high_temp))
