print("Python using oops concept")

class Dog:                                           # creating dog class
    species = "Animal"                               # class attributes

    def __init__(self, name, age, breed, color ):
        self.name = name                             # instance attributes
        self.age = age
        self.breed = breed
        self.color = color


misty = Dog("misty", 9, "Havanese", "white")                                 # object creation
rocky = Dog("rocky", 6, "German Shepherd", "brown")                          # object creation
print(misty)
print(rocky)
print(misty.age)
print(rocky.breed)
print(misty.species)
print(rocky.species)

print(misty == rocky )                                                # two different objects (False)
