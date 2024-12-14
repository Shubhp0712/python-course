class employee : # Parent class

    company = "Google"
    name = "Shubh"

    def show(self):
        print(f"Hi my name is {self.name} and I work in {self.company}")

class manager(employee): # Child class
    name = "Sunderlal"

    def showmanager(self):
        print("I am a manager.")


a = employee()
a.show() # Here we can't access showmanager() method because it is not present in employee class

b = manager() # By child class object we can access all the methods of parent class as well as child class
b.show()
b.showmanager()