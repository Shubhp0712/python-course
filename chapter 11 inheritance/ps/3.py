class Employee:
    salary = 1678
    increment = 25

    @property
    def salaryafterincrement(self):
        return (self.salary + ((self.salary*self.increment)/100))
    
    @salaryafterincrement.setter
    def salaryafterincrement(self, salary):
        self.increment = ((salary/self.salary)-1)*100

e = Employee()
print(e.salaryafterincrement)

e.salaryafterincrement = 2047.16
print(e.increment)

