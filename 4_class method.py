class Employee: 
    no_of_leaves = 10
    
    def __init__(self,name,eno):
        self.name = name 
        self.eno = eno
    
    def printdetail(self): 
        return f"Employee name is {self.name} with e_no as {self.eno}"
    
    @classmethod     #here it is like, we created a function can dominate and reflex the class which is something virtual for object to digest.
    def change_leave(cls,newleave):
        cls.no_of_leaves = newleave

e1 = Employee('adeeb','1234')
print(e1.no_of_leaves)  #op = 10
e1.change_leave(25)
print(e1.no_of_leaves)   #op = 10



