from time import time
from time import ctime


def format_ft_time():
    t = time()
    format_t = f'{t:,.4f}'  # f-string으로 숫자에 콤마 넣고 소숫점 4자리까지 확인
    str_time = ctime(t)  # "Sun Aug 25 21:38:08 2024"
    split_time = str_time.split()  # ['Sun', 'Aug', '25', '21:39:32', '2024']
    word = "Seconds since January 1, 1970:"
    notation = "in scientific notation"
    print(word, format_t, "or", "%.2e" % t, notation)
    print(split_time[1], split_time[2], split_time[4])


format_ft_time()
