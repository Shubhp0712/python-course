class Employee:
    degignation = "General Manager"
    specialization = "Software Development"
    language = "Python"

    def greet(self): # Here we pass self argument so it will not give an error.
        print(f"Hello Good morning, {self.name}")

    def Info(self): # This method will give an error because it is not taking any argument. So, it will give an error.If we want to use this method, then we have to pass the self argument.
        print(f"My name is {self.name}. I am working as a {self.degignation} in the field of {self.specialization}. I am expert in {self.language}.")


shubh = Employee()
shubh.name = "Shubh"

shubh.greet()
shubh.Info() # It excatly equals to Employee.Info(shubh) because shubh is the instance of Employee class. So, it will pass the shubh as the self argument.