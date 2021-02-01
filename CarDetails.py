class Car:
    def __init__(self, color, mileage):
        self.color =  color
        self.mileage = mileage

    def __str__(self):
        return f"{self.color} has {self.mileage} miiles "


Creta = Car(color = "blue" , mileage = 20000 )
swift = Car( color= "red" , mileage= 30000 )

for car in (Creta,swift):                     # second approach
    print(f"{car.color} has {car.mileage} miiles")

print(Creta.__str__())
print(swift.__str__())

