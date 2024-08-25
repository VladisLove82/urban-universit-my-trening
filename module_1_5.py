immutable_var = 1,2,3,4,5,6,7, "a", "b"
print(immutable_var)
#immutable_var = [0] = 25 #tuple(Кортеж) - не может быть изменён потому, что он не поддерживает обращение по элементам
print(immutable_var)
mutable_list = ["juice", "apple", "bread", "meat"]
mutable_list [0] = 'peach'
mutable_list [3] = 'cherry'
print(mutable_list)