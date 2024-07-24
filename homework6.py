my_dict={'Anna': 1997,'Boris': 2003,'Maria': 2012}
print(my_dict)
print(my_dict['Anna'])
my_dict['Victor']=1979
print(my_dict['Victor'])
my_dict.update({'Sonya': 2005,'Ivan': 2007})
a=my_dict.pop('Anna')
print(a)
print(my_dict)
my_set={1,2,3,3,4,5,1,2,3}
print(my_set)
my_set.add(6)
my_set.add(7)
my_set.discard(3)
print(my_set)