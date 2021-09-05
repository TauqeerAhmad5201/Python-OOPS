class Employee: 
    no_of_leaves = 10
    
    def __init__(self,name,eno):
        self.name = name 
        self.eno = eno
    
    def printdetail(self): 
        return f"Employee name is {self.name} with e_no as {self.eno}"
    
    @staticmethod
    def printtemplate(string):
        print(f"The template number is {string}")    

e1= Employee('Tauqeer', 'FH5654')
Employee.printtemplate('THT8118')   #we have to call out using class name 


