#here we learnt that, when data passed to constructor, it can only be accessed but cannot be changed even we are changing it using instance variable 
class Employee:

    def __init__(self,fname,lname):
        self.fname = fname   #updating using instance, NOT WORKING 
        self.lname = lname
        # self.email = f"{self.fname}{self.lname}@gmail.com"  #if we try to update instance variable, it will not work because it is in constructor, it works only with functions 

    def email(self):
        return f"{self.fname}{self.lname}@gmail.com"

e1 = Employee("Tauqeer","Ahmad")
e1.fname = "Adeeb"
#at this level, we will get the output as per the latest update using instance variable because for editing constructor init, we have to pass arguments into class name which is not possible everytime 
print(e1.email())