print("Python using oops concept")

class Dog:                                           # creating dog class
    species = "Animal"                               # class attributes

    def __init__(self, name, age, breed, color ):
        self.name = name                             # instance attributes
        self.age = age
        self.breed = breed
        self.color = color

    def printAge(self):                               # instance method
        print(f"{self.name} is {self.age} years old" )



misty = Dog("misty", 9, "Havanese", "white")                                 # object creation
rocky = Dog("rocky", 6, "German Shepherd", "brown")                          # object creation

misty.printAge()

print(misty == rocky )                                                # two different objects (False)
