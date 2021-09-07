#super() works with __init__

class Principal:
    def __init__(self):
        print('Leadership of Principal')

    def printdetails(self):
        print('Principal leads everyone')

class HOD(Principal):
    def __init__(self):
        super().__init__()
        print('Leadership of HOD')

class Proctor(Principal):
    def __init__(self):
        print('Leadership of Proctor')

class CR(HOD,Proctor):
    def __init__(self):
        super().__init__()
        print('Init of CR Working')
c1 = CR()
c1.printdetails()
