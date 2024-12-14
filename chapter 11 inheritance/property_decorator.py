class employee:

    @property # getter method
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter # setter method
    def name(self, value):
        self.fname = value.split(" ")[0]  # Here we are splitting the value of name and storing it in fname and lname
        self.lname = value.split(" ")[1]

# Here this is concept of abstraction where we are hiding the implementation of the code and encapsulating the code by wrapping it in a class

e = employee()
e.name = "Shubh patel"

print(e.name)