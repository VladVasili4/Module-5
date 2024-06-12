class House:
    def __init__(self, numberOfFloors):
        self.numberOfFloors = 0
    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors += int(floors)
        print(self.numberOfFloors)


dom = House(3)
dom.setNewNumberOfFloors(5)

