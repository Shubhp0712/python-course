class program:

    a = 10

# When we don't want to change the value of a we can use class method we can use class method @classmethod
# @classmethod is used to access the class variable

    @classmethod
    def show(cls): # Here cls is used to access the class variable instead of self
        print(f"The value of a is {cls.a}")

o = program()
o.a = 20 # Here we are changing the value of a

o.show() # Here the value of a will be 20 because we have changed the value of a.   