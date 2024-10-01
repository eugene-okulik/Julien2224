my_dict = {'tuple': (1, 'julia', True, 5.34, None),
           'list': [2, 'julia2', False, None, 3.98],
           'dict': {'one': 'julia3', 2: 4, (1, 2, 3): True, 'four': None, 5: 4.98},
           'set': {1, 2.34, False, 'julia4', 1, 2}}

print(my_dict['tuple'][-1])  # вывод на экран последнего элемента 'tuple'
my_dict['list'].append('new_element')  # добавление в 'list' одного элемента
my_dict['list'].pop(1)  # удаление второго элемента 'list'
my_dict['dict']['i am a tuple'] = 12345  # добавление элемента с ключом 'i am a tuple' в 'dict'
del my_dict['dict']['one']  # удаление первого эелемента 'dict'
my_dict['set'].add('123')  # добавление элемента '123' в 'set'
my_dict['set'].remove(1) # удаление элемента 1 из 'set'
print(my_dict)  # вывод на экран всего словаря
