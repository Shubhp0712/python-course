class Employee:
    degignation = "General Manager"
    specialization = "Software Development"
    language = "Python"

    # def __init__(self): # Here we using constructor without any argument.
    #    print("Constructor is called")


    def __init__(self,name,degignation,specialization,language): # Constructor is called when we create the object of the class.It is called automatically.it is known as dunder method.
        self.name = name
        self.degignation = degignation
        self.specialization = specialization
        self.language = language

        print("Constructor is called")
   

# shubh = Employee() # the another way to use the constructor is to pass the argument in the constructor.
# shubh.name = "Shubh"

shubh = Employee("Shubh", "General manager", "Software Developer", "Python") # Here we pass the argument in the constructor.

print(shubh.name, shubh.degignation, shubh.specialization, shubh.language)

