class Student: 
    no_of_leaves = 8
    pass 

adeeb = Student()
anas = Student()

adeeb.name = 'adeeb'
adeeb.section = 'A'

anas.name = 'anas'
anas.section = 'B'

print(anas.name)
print(anas.no_of_leaves)
print(Student.__dict__)
print(anas.__dict__)

Student.no_of_leaves = 10
print(anas.no_of_leaves)
anas.no_of_leaves = 12  # here just one variable is being created inside anas, nothing affecting the class variable

print(Student.no_of_leaves)   # o/p = 10 
print(anas.no_of_leaves)       # o/p = 12

print(Student.__dict__)
print(anas.__dict__)