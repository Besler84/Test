print()
print("Methoden erstellen")
print()

class Car:
    def __init__(self):
        self.car_brand = None
        self.horse_power = None
        self.color = None
        self.x_position = 5
        self.y_position = 5
    def drive(self, x, y):
        self.x_position += x
        self.y_position += y


car01 = Car()
car02 = Car()
car03 = Car()

print(car01.x_position)
print(car01.y_position)
print()

print(car02.x_position)
print(car02.y_position)
print()

print(car03.x_position)
print(car03.y_position)
print()
