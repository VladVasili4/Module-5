class Building:
    total = 0
    def __init__(self, adres):
        Building.total += 1 # Добавляем единицу к счетчику, при инициализации нового объекта
        print('Количество объектов (зданий) :', Building.total)
        self.adres = adres


    def __str__(self):
        return f'Adress : {self.adres}'

    def __call__(self):
        return self.adres


House1 = Building(1)
House2 = Building(2)
House3 = Building(2)
House4 = Building(3)
#
# house_ = []
# def build_():
#     for i in range(1, 40):
#         global house_
#         house_.append('house'+str(i))
#     print(house_)
#     house_ = tuple(house_)
# build_()
#
# print(house_)
#
# result = [Building(*data) for data in house_]
# for info in result:
#     print(info)
# print()
# for info in result:
#     print(info())


#
# class Resistor:
#     total = 0
#     def __init__(self, resist, unit, power=None):
#         Resistor.total += 1  # Добавляем единицу к счетчику, при инициализации нового объекта
#             print('Количество объектов (зданий) :', Resistor.total)
#             self.resist = resist
#             self.unit = unit
#             self.power = power
#
#     def __str__(self):
#         return f'сопротивление {self.resist} {self.unit} {self.power}ватт'
#
#     def __call__(self):
#         return self.resist, self.unit, self.power
#
#
# lst = [(5, 'om', 10), (15, 'Kom', 3), (27, 'Mom', 10)]
# result = [Resistor(*data) for data in lst]
# for info in result:
#     print(info)
# print()
# for info in result:
#     print(info())