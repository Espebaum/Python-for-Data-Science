import pandas as pd
import numpy as np

# -> Dataset: (You have to adapt the type of return according to your library)
def load(path: str):
    df = pd.read_csv(path)
    print(df)
    print("Loading dataset of dimensions", df.shape)
    print(df['country'])