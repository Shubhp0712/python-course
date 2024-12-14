class father:
    
    def fmethod(self):
        print("I am a father class")


class mother:

    def mmethos(self):
        print("I am a mother class")


class child(father, mother):

    def cmethod(self):
        print("I am a child class")


# Here it is called mutiple inheritance because the child class inherits more than one parent class


a = father()
a.fmethod()
# a.mmethod() # This will give an error because mmethod() is not present in father class

b = mother()
b.mmethos()


c = child()
c.fmethod()
c.mmethos()
c.cmethod()