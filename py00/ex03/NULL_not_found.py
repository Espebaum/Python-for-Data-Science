def NULL_not_found(object: any) -> int:
    t = type(object)
    # NoneType이면서 value가 None이 아닌 경우는 존재하지 않음
    if str(t) == "<class 'NoneType'>":
        print("Nothing:", object, t)
    # object value가 Null이 아니면 Type not Found를 출력
    elif str(t) == "<class 'float'>":
        if object == object:
            print("Type not Found")
            return 1
        else:
            # NaN은 자기 자신과 같지 않다.
            # float의 Null 값으로 Nan을 고려할 수 있다.
            print("Cheese:", object, t)
    elif str(t) == "<class 'int'>":
        if object != 0:
            print("Type not Found")
            return 1
        else:  # int의 Null 값 0
            print("Zero:", object, t)
    elif str(t) == "<class 'str'>":
        if object != '':
            print("Type not Found")
            return 1
        else:  # str의 Null 값 빈 문자열
            print("Empty:", object, t)
    elif str(t) == "<class 'bool'>":
        if object is True:
            print("Type not Found")
            return 1
        else:  # bool의 Null 값 False
            print("Fake:", object, t)
    return 0
