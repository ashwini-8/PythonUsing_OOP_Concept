class Car:
    def __init__(self, color, mileage):
        self.color =  color
        self.mileage = mileage

    def __str__(self):
        return f"{self.color} has {self.mileage} miiles "

Creta = Car("blue" , 20000 )
swift = Car("red" , 30000 )
print(Creta.__str__())
print(swift.__str__())