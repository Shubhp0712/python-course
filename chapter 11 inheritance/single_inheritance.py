class parent:

    def preant(self):
        print("I am a parent class")

class child(parent):

    def child(self):
        print("I am a child class")

# Here it is called single inheritance because the child class inherits only one parent class

a = parent()
a.preant()

b = child()
b.child()
b.preant()