import numpy as np
import matplotlib.pyplot as plt


def ft_invert(nd):
    """
    numpy 배열을 list로 바꾼 후 전치시킵니다.
    """
    lst = nd.tolist()
    lst_A = list(reversed(lst))
    n_A = np.array(lst_A, dtype=np.int32)
    # print(n_A)
    plt.imshow(n_A)
    plt.show()
    