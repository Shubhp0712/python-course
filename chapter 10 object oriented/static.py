class Employee:
    degignation = "General Manager"
    specialization = "Software Development"
    language = "Python"

    @staticmethod
    def greet(): # Here if don't pass the self argument, We can use static method.
        print(f"Hello, Good morning")

    def Info(self): # This method will give an error because it is not taking any argument. So, it will give an error.If we want to use this method, then we have to pass the self argument.
        print(f"My name is {self.name}. I am working as a {self.degignation} in the field of {self.specialization}. I am expert in {self.language}.")


shubh = Employee()
shubh.name = "Shubh"

shubh.greet() # It will not give an error because we are using static method.
shubh.Info() # It excatly equals to Employee.Info(shubh) because shubh is the instance of Employee class. So, it will pass the shubh as the self argument.