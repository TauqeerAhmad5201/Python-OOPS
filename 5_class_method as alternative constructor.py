class Employee: 
    no_of_leaves = 10
    
    def __init__(self,name,eno):
        self.name = name 
        self.eno = eno
    
    def printdetail(self): 
        return f"Employee name is {self.name} with e_no as {self.eno}"
    
    @classmethod 
    def change_leave(cls,newleave):
        cls.no_of_leaves = newleave
    
    # @classmethod 
    # def from_dash(cls,string):
    #     params = string.split("-")  #list will be created over here
    #     print(params)
    #     return cls(params[0],params[1])

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))   #putting star in split function directly makes it to be passed as argument

e1 = Employee.from_dash('adeeb-1234')
print(e1.name)
print(e1.eno)



