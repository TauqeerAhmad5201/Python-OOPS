class A: 
    def __init__(self):
        print('Class A init is working')

    def feature1(self):
        print('Feature 1 is working')
    
    def feature2(self):
        print('Feature 2 is working')

class B():  
    def __init__(self):
        print('Class B init is working')

    def feature3(self):
        print('Feature 3 is working')
    
    def feature4(self):
        print('Feature 4 is working')

class C(B,A):  #MRO
    def __init__(self):
        super().__init__()
        print('Class C init is working')

    def feature5(self):
        print('Feature 5 is working.')

c1 = C()

