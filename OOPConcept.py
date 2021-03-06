print("Python using oops concept")

class Dog:                                           # creating dog class
    species = "Animal"                               # class attributes

    def __init__(self, name, age ):
        self.name = name                             # instance attributes
        self.age = age

    def __str__(self):  # instance method
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

misty = JackRussellTerrier("misty", 9)                                 # object creation
rocky = Dachshund("rocky", 6)
jeo = Bulldog("jeo", 3)

print(misty.speak("bhow bhow"))
print(misty.speak())

print(type(misty))
print(isinstance(jeo, Dachshund))
