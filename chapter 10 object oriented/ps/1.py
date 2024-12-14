class programmer:

    company = "Microsoft"

    def __init__(self,name,age,language,degicnation,salary):
        self.name = name
        self.age = age
        self.language = language
        self.degicnation = degicnation  
        self.salary = salary


shubh = programmer("Shubh", 20, "Python", "Software Developer", 50000)
print(f"My name is {shubh.name}. I am {shubh.age} years old. I am working as a {shubh.degicnation} in the company {shubh.company}. I am expert in {shubh.language}. I am getting {shubh.salary} per month.")

samarth = programmer("Sam", 21, "Java", "Web Developer", 60000)
print(f"My name is {samarth.name}. I am {samarth.age} years old. I am working as a {samarth.degicnation} in the company {samarth.company}. I am expert in {samarth.language}. I am getting {samarth.salary} per month.")