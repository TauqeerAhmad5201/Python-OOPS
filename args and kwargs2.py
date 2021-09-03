def intro(**data):  #Here it always accepts dictionary, otherwise if not provided, then it converts into dictionary. 
    print('\nData types : ',type(data))
    print(data.items())
    for key,value in data.items():
        print('{} is {}'. format(key,value))

intro(Firstname = "Adeeb", lastname = 'Ahmad' , Phone = 3534543)
intro(Firstname = 'Tauqeer', lastname = "Ahmad" , Country = "India", email = 'hellotauqeer@gmail.com')

mydict = {'Firstname' : 'Anas', 'Lastname': 'Akhtar', 'Phone' : 7564564}
# intro(mydict)
intro(**mydict)