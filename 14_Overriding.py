class A: 
    classvar1 = "I am class variable in class A" #CLASSVARIABLE

    def __init__(self):
        self.var1 = "I am inside Class A's Constructor"
        self.classvar1 = "Instance var in class A" #INSTANCEVARIABLE
        self.special = "Special Variable from Class A"

class B(A):
    classvar1 = "I am class variable in class B"     
    #CLASSVARIABLE

    def __init__(self):
        super().__init__()    #simply super() help us to access the method of parent class which help in getting variables so far.
        self.var1 = "I am inside Class B's Constructor"
        self.classvar1 = "Instance var in class b" #INSTANCEVARIABLE

a1 = A()
b1 = B()

print(b1.classvar1)
print(a1.special)
#so here to learn is that priority level 
# Priority 1 - instance variable(object.variable)
# Priority 2 - class variable
# print(b1.special)