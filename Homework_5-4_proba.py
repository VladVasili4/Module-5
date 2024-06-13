class Building:
    total = 0
    def __init__(self):
        Building.total += 1 # Добавляем единицу к счетчику, при инициализации нового объекта
        print('Количество объектов (зданий) :', Building.total)


# House1 = Building()
# House2 = Building()
# House3 = Building()
# House4 = Building()

house_ = []
def build_():
    for i in range(1, 40):
        global house_
        house_.append('house'+str(i))
        # house_ = Building()
    print(house_)
build_()

print(house_)
