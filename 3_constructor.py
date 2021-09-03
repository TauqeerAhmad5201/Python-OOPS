class Employee: 
    no_of_leaves = 10
    
    def __init__(self,name,eno):
        self.name = name 
        self.eno = eno
    
    def printdetail(self): 
        return f"Employee name is {self.name} with e_no as {self.eno}"

e1 = Employee('adeeb','1234')
print(e1.printdetail())



