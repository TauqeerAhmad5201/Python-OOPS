class data: 
    var = 1 #public data -> can be accesss by many 
    _mydata = 100 #protected data -> can be accessed only by instance object or object of derived class 
    __pvtdata = 1000 #private data -> can only be accessed by name-mangling which means _classname__pvtvariable

class inherited(data):
    pass 

class test(inherited): 
    pass 

d1 = data()
e1 = inherited()
t1 = test()
print(d1._data__pvtdata)  #name-mangling for pvt data  ._classname__pvtvariable
print(e1._mydata)
print(d1.var)
print(d1._mydata)
print(t1._mydata)