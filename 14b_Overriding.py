#here we learnt that, when data passed to constructor, it can only be accessed but cannot be changed even we are changing it using instance variable 
class Employee:

    def __init__(self,fname,lname):
        self.fname = fname          #updating using instance, NOT WORKING 
        self.lname = lname
        self.email = f"{self.fname}{self.lname}@gmail.com"  #if we try to update instance variable, it will not work because it is in constructor, it works only with functions 

    # def email(self):
    #     return f"{self.fname}{self.lname}@gmail.com"

e1 = Employee("Tauqeer","Ahmad")
print(e1.fname, e1.lname , e1.email)
e1.fname = "Anas"
e1.lname = "Akhtar"
#observe carefully that fname and lname changed using instance variable and email is still generated will old fname and lname means constructor can't be edited 
print(e1.fname, e1.lname , e1.email)