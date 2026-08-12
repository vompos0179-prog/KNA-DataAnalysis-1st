# "================================================="
print("===============================")

# 1. 현재 경로에 가상환경 설정
## python -m venv .venv

# 2. 활성화
## source .venv/Scripts/activate.ps1
## 이후, pip install pandas 입력

import os
import pandas as pd

# 실습 예제 1) csv 파일 불러오기

filepath = os.path.join("data", "12_metro_small.csv")  # "data/12_metro_small.csv"

try:
    df = pd.read_csv(
        filepath,
        encoding="utf-8",
        sep=",",
        index_col="측정시각",
        nrows=5,
        usecols=["측정시각", "가동상태"],
    )
    print(df.shape)  # (30, 7)

    print(df.head(10))
except FileNotFoundError:
    print(f"파일이 없습니다 : {filepath}")
