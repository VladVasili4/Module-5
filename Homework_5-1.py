class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to (self, new_floor):
        self.new_floor = int(new_floor)
        if 1 <= self.new_floor <= self.number_of_floors:
            for i in range(1, self.new_floor + 1):
                print(i)
        else: print('Такого этажа не существует')


h1 = House('Lenina7', 10)
h2 = House('Matrosova5', 5)
h1.go_to(6)
h2.go_to(7)
h1.go_to(-1)
h2.go_to(4)