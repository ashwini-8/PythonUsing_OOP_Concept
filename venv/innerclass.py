class Person:
    def __init__(self,name):
        self.name = "Ashwini"
        self.details = self.Adult()

    def show(self):
        print("Name: " , self.name)

    class Adult:
        def __init__(self):
            self.name = "Ashwini Patil"
            self.id  = "101"

        def display(self):
            print("Name: ", self.name)
            print("ID:" , self.id)

outer  = Person("Ashwini")
outer.show()

person_details = outer.details
person_details.display()