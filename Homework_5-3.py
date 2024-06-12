class Building:
    def __init__(self, buildingType, numberOfFloors):
        self.buildingType = str(buildingType)
        self.numberOfFloors = int(numberOfFloors)

    def __eq__(self, other):
        return self.buildingType == other.buildingType and self.numberOfFloors == other.numberOfFloors

my_home = Building('house',10)
my_work = Building('office',4)
son_home = Building('house',10)
son_work = Building('office',7)

print(my_home == my_work)
print(my_home == son_home)
print(son_home == son_work)
print(my_work == son_work)



