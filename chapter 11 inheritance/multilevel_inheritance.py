class shape:

    def show(self):
        print("This is a shape")

class square(shape):
    
    def showsquare(self):
        print("This is a square Shape")

class rectangle(square):

    def showrectangle(self):
        print("This is a rectangle Shape")


# Here it is called multilevel inheritance because the child class inherits the parent class which is already inherited by another class


a = shape()
a.show()

b = square()
b.show()
b.showsquare()

c = rectangle()
c.show()
c.showsquare()
c.showrectangle()