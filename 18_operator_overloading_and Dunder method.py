class Employee: 

    def __init__(self,name,role,salary):
        self.name = name
        self.role = role 
        self.salary = salary
    
    def printdetails(self):
        return f"Employee name with {self.name}, {self.salary} is set as {self.role}"
    
    def __add__(self,other):
        return self.salary + other.salary

e1 = Employee("Harry","Software Engineer", 80000)
e2 = Employee("Anas","Manager", 70000)
# e3 = Employee("Adeeb","Manager Senior", 90000)

print(e1+e2)
# print(e1+e2+e3)  #problem, how to deal with three

print(e1.printdetails(),e2.printdetails())
