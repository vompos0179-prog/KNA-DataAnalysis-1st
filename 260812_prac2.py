import pandas as pd

# ============================================================
# 실습 1. head() / tail()로 디지털 신호 데이터 살펴보기
# ============================================================

print("=" * 60)
print("실습 1. 디지털 신호 데이터 살펴보기")
print("=" * 60)

# CSV 파일 불러오기
df_digital = pd.read_csv("data/12_metro_digital.csv")

# 처음 5줄 보기
print("\n[head()]")
print(df_digital.head())

# 마지막 5줄 보기
print("\n[tail()]")
print(df_digital.tail())

# 처음 10줄 보기
print("\n[head(10)]")
print(df_digital.head(10))


# ============================================================
# 실습 2. head() / tail() 행 개수 조절
# ============================================================

print("\n" + "=" * 60)
print("실습 2. 행 개수 조절")
print("=" * 60)

# 처음 1줄
print("\n[head(1)]")
print(df_digital.head(1))

# 처음 10줄
print("\n[head(10)]")
print(df_digital.head(10))

# 마지막 7줄
print("\n[tail(7)]")
print(df_digital.tail(7))

# 데이터보다 큰 숫자를 넣어보기
print("\n[head(500)]")
print(df_digital.head(500))
