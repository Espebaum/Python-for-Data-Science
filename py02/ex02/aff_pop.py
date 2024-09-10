from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd

def main():
    df = load("population_total.csv")
    df_korea = df.loc['South Korea'].str.replace('M', '').astype(float) * 1e6  # 'M' 제거 후 숫자로 변환
    df_france = df.loc['France'].str.replace('M', '').astype(float) * 1e6  # 'M' 제거 후 숫자로 변환
    
    # 데이터 결합
    df_combined = pd.concat([df_korea, df_france], axis=1)
    
    # 인덱스를 숫자로 변환
    k_index = pd.to_numeric(df_korea.index, errors='coerce')
    kf_index = k_index[(k_index % 40 == 0)].dropna().astype(str)

    f_index = pd.to_numeric(df_france.index, errors='coerce')
    ff_index = f_index[(f_index % 40 == 0)].dropna().astype(str)

    # 각 데이터 필터링 후 값 추출
    kf_values = df_korea.loc[kf_index].values
    ff_values = df_france.loc[ff_index].values

    # 두 개의 시리즈를 각각 플롯
    plt.plot(kf_index, kf_values, label='South Korea')
    plt.plot(ff_index, ff_values, label='France')

    # y축 틱을 20M, 40M, 60M으로 제한
    plt.yticks([20e6, 40e6, 60e6], ['20M', '40M', '60M'])
    
    # 그래프 레이블 및 제목 설정
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population Projection')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
