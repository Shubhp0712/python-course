class Student:

    age = 18 # class variable or attribute
    std = 12

shubh = Student()
shubh.name = "Shubh" # instance variable or attribute
shubh.age = 20 
# Here If we define the instance variable with the same name as the class variable, then the instance variable will be used.Before the instance variable was not defined, so the class variable was used. Because instance variable has higher priority than class variable.

# Instance attributes, take preference over class attributes during assignment & retrieval.
print(shubh.name, shubh.age, shubh.std) 
