# Создайте новый класс Buiding с атрибутом total
# Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества созданных объектов класса Building total
# В цикле создайте 40 объектов класса Building и выведите их на экран командой print
class Building:
    total = 0


    def __init__(self,name):
        Building.total += 1 # Добавляем единицу к счетчику, при инициализации нового объекта
        self.count_(name)
        print('Количество объектов (зданий) :', Building.total)


    def count_(self, name):
        self.name = name
        print('Построен новый дом :', self.name)
        return self.name


house = []
x = 0
y = 0

def build_():
    for i in range(1, 41):
        global house
        house.append('house'+str(i))
        *x, y = house
        y = Building(house[-1])


build_()

