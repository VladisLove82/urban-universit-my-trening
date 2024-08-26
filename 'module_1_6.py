my_dict = {"Vasya": 1975, "Egor": 1999, "Masha": 2002}
print(my_dict)
print(my_dict['Egor'])
my_dict.update({'Yaroslav': 2005, 'Andrey': 1992})
print(my_dict)
name = my_dict.pop('Masha')
print(my_dict)


my_set = {1, 1, 1, 2, 3, 4, 4, 6, 7, 0, 1.2, 1.2, "string", True, "aplle"}
print(my_set)
list_a = {1, 1, 1, 2, 3, 4, 4, 6, 7, 0, 1.2, 1.2, "string", True, "apple", (1, 2, 3, 2.1)}
list_a.add(10)
list_a.add(14)
print(list_a)
my_set.remove(1)
my_set.discard(1.2)
print(my_set)
