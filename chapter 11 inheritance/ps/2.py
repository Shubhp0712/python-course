class animals:

    pass

class pets(animals):

    pass 

class dog(pets):

    def bark(self):
        print("The dog is barking.")

d = dog()
d.bark()