from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd

def main():
    df = load("population_total.csv")
    df_korea = df.loc['South Korea'].str.replace('M', '').astype(float) * 1e6  # 'M' 제거 후 숫자로 변환
    df_france = df.loc['France'].str.replace('M', '').astype(float) * 1e6  # 'M' 제거 후 숫자로 변환
    
    # print(df_korea)
    df_korea.index = pd.to_numeric(df_korea.index, errors='coerce')
    filtered_korea = df_korea.loc[1800:2050]
    print(filtered_korea)

    df_france.index = pd.to_numeric(df_france.index, errors='coerce')
    filtered_france = df_france.loc[1800:2050]

    k_values = filtered_korea.values
    f_values = filtered_france.values

    # # # 두 개의 시리즈를 각각 플롯
    plt.plot(filtered_korea.index, k_values, label='South Korea')
    plt.plot(filtered_france.index, f_values, label='France')

    # # # # y축 틱을 20M, 40M, 60M으로 제한
    plt.yticks([20e6, 40e6, 60e6], ['20M', '40M', '60M'])
    plt.xticks([1800, 1840, 1880, 1920, 1960, 2000, 2040])

    # # # # 그래프 레이블 및 제목 설정
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population Projections')
    plt.legend(loc='lower right')
    plt.show()

if __name__ == "__main__":
    main()
