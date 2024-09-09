import pandas as pd
from pandas import DataFrame

def load(path: str) -> DataFrame:
    df = pd.read_csv(path, index_col=0)
    print("Loading dataset of dimensions", df.shape)
    pd.set_option('display.max_columns', 8)  
    # 한 번에 출력할 최대 열 수
    return df