my_dict = {'Pety': 1996 , 'Zhora': 2003 , 'Max': 2000 , 'Nikita': 1999 , 'Fedy': 1993 , 'Katy': 2001}
print(my_dict)
print(my_dict['Nikita'])
my_dict['Masha'] = 1997
print(my_dict['Masha'])
my_dict.update({'Alex': 2004,
                'Irina': 1998})
print(my_dict)
del my_dict['Pety']
print(my_dict)

my_set = {1,1,1,1,7,7,5.6,7,7,7,'Roma','Roma','Roma','Roma','Fedy','Fedy','Fedy',1,True,1,True,5,5,5.6,5.6,5,5}
print(my_set)
my_set.add(29)
my_set.add(27)
print(my_set)
my_set.remove(5.6)
print(my_set)
