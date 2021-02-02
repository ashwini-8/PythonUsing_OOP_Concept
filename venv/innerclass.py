class Person:
    def __init__(self,name):
        self.name = "Ashwini"
        self.detailsofAdult = self.Adult()
        self.detailsOfStudent  = self.Student()

    def show(self):
        print("Name: " , self.name)

    class Adult:
        def __init__(self):
            self.name = "Ashwini Patil"
            self.id  = "101"

        def display(self):
            print("Name: ", self.name)
            print("ID:" , self.id)

    class Student:
        def __init__(self):
            self.name = "fniehfi"
            self.standard = "Graduate"

        def print(self):
            print("Name: ",self.name)
            print("Standard: ", self.standard)

outer  = Person("Ashwini")
outer.show()

person_details = outer.detailsofAdult
person_details.display()

student_Details  = outer.detailsOfStudent
student_Details.print()