class shape:

    def __init__(self):
        print("Constructor of shape class")

    def show(self):
        print("This is a shape")

class square(shape):
    
    def __init__(self):
        super().__init__()
        print("Constructor of square class")

    def showsquare(self):
        print("This is a square Shape")

class rectangle(square):

    def __init__(self):
        super().__init__()
        print("Constructor of rectangle class")

    def showrectangle(self):
        print("This is a rectangle Shape")

# Here we are using super() method to call the constructor of parent class\
# super() method is used to call the constructor of parent class

c = rectangle() # when we create the object of child class then the constructor of all the parent class will be called using super() method
