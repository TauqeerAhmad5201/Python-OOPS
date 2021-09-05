class A: 
    def feature1(self):
        print('Feature 1 is working')
    
    def feature2(self):
        print('Feature 2 is working')

class B(A):  #inheritance
    def feature3(self):
        print('Feature 3 is working')
    
    def feature4(self):
        print('Feature 4 is working')

a1 = A()
b1 = B()
print('Printing from class B')
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()
print('Printing from class A')
a1.feature1()
a1.feature2()