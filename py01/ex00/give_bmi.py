import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:

    np_h = np.array(height) # (2, )
    np_w = np.array(weight) # (2, )

    if np_h.shape != np_w.shape:
        raise ValueError("키 배열과 몸무게 배열의 형태가 같아야 한다.")

    if not (np.issubdtype(np_h.dtype, np.number) and np.issubdtype(np_w.dtype, np.number)):
        raise ValueError("키 배열과 몸무게 배열의 값이 잘못되었다.")

    bmi = np_w / (np_h ** 2)
    # print(bmi, type(bmi))

    bmi_list = bmi.tolist()
    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    
    if not isinstance(limit, int):
        print(f'기준이 정수가 아니다. limit: {limit}')
        exit()
    
    for b in bmi:
        if not isinstance(b, (int, float)):
            print(f'bmi 값이 잘못되었다. bmi: {b}')
            exit()
    
    limit_list = []
    for b in bmi:
        if b > limit:
            limit_list.append(True)
        else:
            limit_list.append(False)
    
    return limit_list


# numpy를 import 하지 않고 파이썬 내장함수만으로 처리


# def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    
#     if len(height) != len(weight):
#         print("키 배열과 몸무게 배열의 길이가 다르다.")
#         exit()

#     for h, w in zip(height, weight): # python zip을 이용한 배열 병렬 순회
#         if not (isinstance(h, (int, float)) and isinstance(w, (int, float))):
#             print(f'키와 몸무게 배열의 값이 잘못되었다. height: {h} weight: {w}')
#             exit()

#     bmi_list = []
#     for h, w in zip(height, weight):
#         bmi = w / (h * h)
#         bmi_list.append(bmi)

#     return bmi_list
