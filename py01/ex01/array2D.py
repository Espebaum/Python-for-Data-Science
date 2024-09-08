import numpy as np

def slice_me(family: list, start: int, end: int) -> list:

    if not isinstance(family, list):
        raise ValueError("family는 반드시 리스트여야 한다.")
    
    if not (isinstance(start, int) and isinstance(end, int)): 
        raise ValueError("start와 end는 반드시 정수여야 한다.")

    f = np.array(family)
    print("My shape is :", f.shape)

    sliced_family = family[start:end]
    sf = np.array(sliced_family)
    print("My new shape is :", sf.shape)

    return sliced_family
