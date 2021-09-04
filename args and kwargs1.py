def adder(*num):    #a tuple is given otherwise converted but yes tuple
    sum = 0 
    
    for n in num:
        sum = sum + n
    
    print("Sum: ",sum)

adder(5,7,4)
adder(5,7,4,6.7)
adder(5,7,4.5,76,34.454)
