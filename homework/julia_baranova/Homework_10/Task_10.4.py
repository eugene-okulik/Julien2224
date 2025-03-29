PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_list = PRICE_LIST.split()

things = new_list[::2]
prices = map(lambda x: int(x.rstrip('р')), new_list[1::2])

things_prices_dict = dict(zip(things, prices))
print(things_prices_dict)
