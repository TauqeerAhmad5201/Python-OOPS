class Employee:
    def __init__(self,fname,lname):
        self.fname  = fname 
        self.lname = lname 

    @property
    def email(self):   #basically it simplifies a function so that it can be called by without () brackets
        return f"{self.fname}{self.lname}@gmail.com"
    
    @email.setter
    def email(self,string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    
e1 = Employee("Tauqeer","Ahmad")
print(e1.email)  #property decotator helping to call function without ()
# e1.fname = "Adeeb"
# print(e1.email)   # due to instance variable, o/p is changed 
e1.email = "Anas.Akhtar@gmail.com"
print(e1.email)
print(e1.fname, e1.lname)

