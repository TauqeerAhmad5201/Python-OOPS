#super() works with __init__
#so here, there is not init usage, so no proper usage of MRO.
class A: 
    def met(self):
        print("Hi I am from Class A")

class B(A):                                                  
    def met(self):                                            #overriding the parent me function
        print("Hi I am from Class B")

class C(A): 
    def met(self):                                             #overriding the parent me function
        print("Hi I am from Class C")

class D(C,B): 
    pass
    # def met(self):
    #     print("Hi I am from Class D")

a = A()
b = B()
c = C()
d = D()

d.met()