from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd

def main():
    df = load("life_expectancy_years.csv")
    # print(df.index)
    df_korea = df.loc['South Korea']
    index = pd.to_numeric(df_korea.index, errors='coerce')
    filtered_index = index[(index % 40 == 0)].dropna().astype(int).astype(str)
    filtered_values = df_korea.loc[filtered_index].values
    plt.plot(filtered_index, filtered_values)
    plt.title("South Korea Life expectancy Projections")
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.show()

if __name__ == "__main__":
    main()