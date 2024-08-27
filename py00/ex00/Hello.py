ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}


def Hello(ft_list, ft_tuple, ft_set, ft_dict):
    # list
    ft_list[1] = 'World!'
    # tuple
    lst1 = list(ft_tuple)
    lst1[1] = 'Korea!'
    ft_tuple = lst1
    # set
    lst2 = list(ft_set)
    if (lst2[0] != 'Hello'):
        lst2[0] = 'Hello'
    lst2[1] = 'Seoul!'
    ft_set = lst2
    # dict
    ft_dict['Hello'] = '42Seoul!'
    return ft_tuple, ft_set


ft_tuple, ft_set = Hello(ft_list, ft_tuple, ft_set, ft_dict)

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
