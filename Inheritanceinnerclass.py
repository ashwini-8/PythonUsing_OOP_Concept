class A:
    def __init__(self):
        self.db = self.Inner()

    def display(self):
        print("in parent class")

    class Inner:
        def display1(self):
            print("inside parent inner class")


class B(A):
    def __init__(self):
        print("in child class")
        super().__init__()

    class Inner(A.Inner):
        def display2(self):
            print("inside child inner class ")


p = B()
p.display()

x = p.db
x.display1()
x.display2()