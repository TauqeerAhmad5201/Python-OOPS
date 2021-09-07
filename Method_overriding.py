class Add: 
    def result(self,x,y):
        print('Addition : ',x+y)

class Multiplication(Add): 
    def result(self,x,y):
        super().result(x,y)
        print('Multiplication : ',x*y)

m = Multiplication()
m.result(12,45)
