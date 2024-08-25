def all_thing_is_obj(object: any) -> int: # type hint
    t = type(object)
    if ( str(t) == "<class 'list'>" ):
        print("List :", t)
    elif ( str(t) == "<class 'tuple'>" ):
        print("Tuple :", t)
    elif ( str(t) == "<class 'set'>" ):
        print("Set :", t)
    elif ( str(t) == "<class 'dict'>" ):
        print("Dict :", t)
    elif ( str(t) == "<class 'str'>" ):
        print(object, "is in the kitchen :", t)
    elif ( str(t) == "<class 'int'>" ):
        print("Type not found")
    return 42 # returned int