class Flower():

    def __init__(self, name, price, living_time, color, delivery_date, stem_length):
        self.name = name
        self.price = price
        self.living_time = living_time
        self.color = color
        self.delivery_date = delivery_date
        self.stem_length = stem_length

    def __repr__(self):
        return f'{self.name}'


class WildFlower(Flower):

    def __init__(self, name, price, living_time, color, delivery_date, stem_length, season):
        super().__init__(name, price, living_time, color, delivery_date, stem_length)
        self.season = season


class GardenFlower(Flower):

    def __init__(self, name, price, living_time, color, delivery_date, stem_length, plant_location):
        super().__init__(name, price, living_time, color, delivery_date, stem_length)
        self.plant_location = plant_location


class GreenFlower(Flower):

    def __init__(self, name, price, living_time, color, delivery_date, stem_length, can_be_dried):
        super().__init__(name, price, living_time, color, delivery_date, stem_length)
        self.can_be_dried = can_be_dried


class Bouquet():
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def show_flowers_list(self):
        return [flower.name for flower in self.flowers]

    def show_full_price(self):
        prices = [flower.price for flower in self.flowers]
        full_price = sum(prices) + 0.1 * sum(prices)
        return round(full_price)

    def show_living_time(self):
        times = [flower.living_time for flower in self.flowers]
        living_time = sum(times) / len(times)
        return round(living_time)

    def sort_by_freshness(self):
        return sorted(self.flowers, key=lambda flower: flower.delivery_date, reverse=True)

    def sort_by_stem_length(self):
        return sorted(self.flowers, key=lambda flower: flower.stem_length, reverse=True)

    def sort_by_price(self):
        return sorted(self.flowers, key=lambda flower: flower.price)

    def find_red_flowers(self):
        return [flower for flower in self.flowers if flower.color == 'red']


chamomile = WildFlower('Ромашка', 1, 30, 'white',
                       '03-03-2025', 12, 'summer')
cornflower = WildFlower('Василек', 2, 31, 'violet',
                        '04.03.2025', 11, 'spring')
poppy = WildFlower('Мак', 5, 60, 'red',
                   '03.03.2025', 12, 'summer')
yarrow = WildFlower('Тысячелистник', 0.5, 150,
                    'white', '03.04.2025', 21, 'autumn')
redRose = GardenFlower('Роза Красная', 3, 10, 'red',
                       '01.01.2025', 21, 'south')
whiteRose = GardenFlower('Роза Белая', 3, 10, 'white',
                         '01.01.2025', 21, 'south')
piony = GardenFlower('Пиона', 12, 12, 'pink',
                     '01.03.2025', 21, 'south')
lily = GardenFlower('Лилия', 13, 9, 'yellow',
                    '01.01.2025', 24, 'west')
eucalyptus = GreenFlower('Эвкалипт', 2, 60, 'green',
                         '01.02.2025', 32, 'True')
salal = GreenFlower('Салал', 21, 90, 'green',
                    '02.02.2025', 50, 'False')
ruscus = GreenFlower('Рускус', 4, 120, 'green',
                     '01.02.2025', 32, 'False')

bouquet1 = Bouquet()
bouquet1.add_flower(salal)
bouquet1.add_flower(piony)
bouquet1.add_flower(redRose)
bouquet1.add_flower(eucalyptus)
bouquet1.add_flower(whiteRose)
list = bouquet1.show_flowers_list()
print(f'Список цветов в букете: {list}')
price = bouquet1.show_full_price()
print(f'Стоимость букета (цветы + упаковка): {price}')
timel = bouquet1.show_living_time()
print(f'Букет увянет через {timel} дней')
sort_fresh = bouquet1.sort_by_freshness()
print(f'Цветы отсортированные по дате доставки (по убыванию): {sort_fresh}')
most_fresh_flower = sort_fresh[0]
print(f'Самый свежий цветок: {most_fresh_flower}')
sort_stem_length = bouquet1.sort_by_stem_length()
print(f'Цветы отсортированные по размеру стебля (по возрастанию): {sort_stem_length}')
sorted_by_price = bouquet1.sort_by_price()
most_expensive_flower = sorted_by_price[0]
print(f'Самый дорогой цветок: {most_expensive_flower}')
red_flowers_from_bouquet = bouquet1.find_red_flowers()
print("Красные цветы в букете:", ",".join(str(f) for f in red_flowers_from_bouquet)
     if red_flowers_from_bouquet else "красных цветов в букете нет")
