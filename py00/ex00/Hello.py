ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

print("Address of list before : ", id(ft_list))
print("Address of tuple before : ", id(ft_tuple))
print("Address of set before : ", id(ft_set))
print("Address of dict before : ", id(ft_dict))

# list
ft_list[1] = 'World!'

# tuple
lst1 = list(ft_tuple)
lst1[1] = 'Korea!'
ft_tuple = lst1

# set
lst2 = list(ft_set)
lst2[1] = 'Seoul!'
ft_set = lst2

# dict
ft_dict['Hello'] = '42Seoul!' 

print("\nAddress of list after : ", id(ft_list))
print("Address of tuple after : ", id(ft_tuple))
print("Address of set after : ", id(ft_set))
print("Address of dict after : ", id(ft_dict))
print('\n')

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)