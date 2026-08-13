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


# ============================================================
# 실습 1. head() / tail()로 데이터 살펴보기
# ============================================================

print("=" * 60)
print("실습 1. metro_small 데이터 살펴보기")
print("=" * 60)

# CSV 파일 불러오기
df_small = pd.read_csv("data/12_metro_small.csv")


# 처음 5줄 보기
print("\n[head()]")
print(df_small.head())


# 마지막 5줄 보기
print("\n[tail()]")
print(df_small.tail())


# 처음 10줄 보기
print("\n[head(10)]")
print(df_small.head(10))


# ============================================================
# 실습 2. head() / tail() 행 개수 조절
# ============================================================

print("\n" + "=" * 60)
print("실습 2. 행 개수 조절")
print("=" * 60)


# 처음 1줄
print("\n[head(1)]")
print(df_small.head(1))


# 처음 10줄
print("\n[head(10)]")
print(df_small.head(10))


# 마지막 7줄
print("\n[tail(7)]")
print(df_small.tail(7))


# 데이터보다 큰 숫자 입력
# 실제 데이터보다 큰 숫자를 입력해도 오류가 발생하지 않음
print("\n[head(500)]")
print(df_small.head(500))


# ============================================================
# 실습 3. shape / columns / dtypes로 구조 파악
# ============================================================

print("\n" + "=" * 60)
print("실습 3. 구조 파악")
print("=" * 60)

print("\n[shape]")
print(df_digital.shape)

print("\n[columns]")
print(df_digital.columns)

print("\n[dtypes]")
print(df_digital.dtypes)


# ============================================================
# 실습 4. 열 이름 / 자료형 점검
# ============================================================

print("\n" + "=" * 60)
print("실습 4. 자료형 점검")
print("=" * 60)

# 설비 센서 데이터 불러오기
df_sensor = pd.read_csv("data/12_equipment_sensor.csv")

print("\n[설비 센서 데이터 자료형]")
print(df_sensor.dtypes)

print("\n[설비 센서 열 이름]")
print(df_sensor.columns)


# ============================================================
# 실습 5. info()로 데이터 건강검진
# ============================================================

print("\n" + "=" * 60)
print("실습 5. info()로 데이터 건강검진")
print("=" * 60)

print("\n[디지털 신호 데이터 info()]")
df_digital.info()

print("\n[설비 센서 데이터 info()]")
df_sensor.info()

# 결측값 개수 확인
print("\n[설비 센서 데이터 결측값 개수]")
print(df_sensor.isna().sum())


# ============================================================
# 실습 6. describe()로 이상 신호 찾기
# ============================================================

print("=" * 60)
print("실습 6. describe()로 이상 신호 찾기")
print("=" * 60)

import pandas as pd

df_compressor = pd.read_csv("data/12_metro_compressor.csv")

print("[describe()]")

print(df_compressor.describe())

print("\n[75%와 최대값 비교]")


# 숫자로 되어 있는 열만 선택한다.
# 측정시각, 가동상태 같은 문자 데이터는 제외된다.
numeric_data = df_compressor.select_dtypes(include="number")


# 숫자형 열을 하나씩 확인한다.
for column in numeric_data.columns:

    # 75% 값을 구한다.
    q75 = numeric_data[column].quantile(0.75)

    # 최대값을 구한다.
    max_value = numeric_data[column].max()

    # 최대값과 75%의 차이를 구한다.
    difference = max_value - q75

    print(
        column,
        "→ 75%:",
        round(q75, 2),
        ", max:",
        round(max_value, 2),
        ", 차이:",
        round(difference, 2),
    )


# ------------------------------------------------------------
# 오일온도의 75%와 최대값 비교
# ------------------------------------------------------------

print("\n[오일온도 확인]")


# 오일온도의 75% 값을 구한다.
oil_q75 = df_compressor["오일온도"].quantile(0.75)

# 오일온도의 최대값을 구한다.
oil_max = df_compressor["오일온도"].max()

# 75%와 최대값의 차이를 구한다.
oil_difference = oil_max - oil_q75


print("오일온도 75% :", round(oil_q75, 6))
print("오일온도 최대값 :", round(oil_max, 6))
print("오일온도 차이 :", round(oil_difference, 6))


# 오일온도 평균은 63.181910
# 오일온도 75% 값은 68.100000
# 오일온도 최대값은 75.000000

# 75%와 최대값의 차이:
# 75.000000 - 68.100000 = 6.900000

# 따라서 과제에서 75%와 최대값의 차이는 6.900000이다.

print("\n[모터전류와 비교]")


# 모터전류의 75% 값
motor_q75 = df_compressor["모터전류"].quantile(0.75)

# 모터전류의 최대값
motor_max = df_compressor["모터전류"].max()

# 75%와 최대값의 차이
motor_difference = motor_max - motor_q75


print("모터전류 75% :", round(motor_q75, 4))
print("모터전류 최대값 :", round(motor_max, 2))
print("모터전류 차이 :", round(motor_difference, 4))


# 모터전류

# 75% = 3.8125
# 최대값 = 6.19

# 차이: 6.19 - 3.8125 = 2.3775


# ============================================================
# [과제 제출용 최종 주석]
# ============================================================

# [실습 6 최종 해석]
#
# 오일온도의 최대값은 75.000000이다.
# 오일온도의 75%는 68.100000이고

# 75.000000 - 68.100000 = 6.900000

# 모터전류는 75%가 3.8125이고, 최대값이 6.19로 차이는 약 2.38이다.

# ============================================================
# 실습 7. 통계량을 문장으로 묘사
# ============================================================

print("\n" + "=" * 60)
print("실습 7. 통계량 문장으로 묘사")
print("=" * 60)

# 오일온도 통계 확인
temperature = df_compressor["오일온도"]

print("\n[오일온도 통계]")

print("평균 :", round(temperature.mean(), 2))
print("최소 :", round(temperature.min(), 2))
print("최대 :", round(temperature.max(), 2))
print("중앙값 :", round(temperature.median(), 2))
print("표준편차 :", round(temperature.std(), 2))


# 통계량을 문장으로 출력
print("\n[통계량 설명]")

print(
    "오일온도는 평균",
    round(temperature.mean(), 2),
    "도이고,",
    "가장 낮은 값은",
    round(temperature.min(), 2),
    "도이며,",
    "가장 높은 값은",
    round(temperature.max(), 2),
    "도이다.",
)

print(
    "중앙값은",
    round(temperature.median(), 2),
    "도이고,",
    "표준편차는",
    round(temperature.std(), 2),
    "이다.",
)


# ============================================================
# 실습 8. 압축기와 디지털 신호 데이터 구조 비교
# ============================================================

print("\n" + "=" * 60)
print("실습 8. 압축기와 디지털 신호 비교")
print("=" * 60)

# 각각 다른 변수에 저장
df_metro_compressor = pd.read_csv("data/12_metro_compressor.csv")

df_metro_digital = pd.read_csv("data/12_metro_digital.csv")


# 압축기 데이터
print("\n[압축기 데이터 - shape]")
print(df_metro_compressor.shape)

print("\n[압축기 데이터 - info]")
df_metro_compressor.info()

print("\n[압축기 데이터 - describe]")
print(df_metro_compressor.describe())


# 디지털 신호 데이터
print("\n[디지털 신호 데이터 - shape]")
print(df_metro_digital.shape)

print("\n[디지털 신호 데이터 - info]")
df_metro_digital.info()

print("\n[디지털 신호 데이터 - describe]")
print(df_metro_digital.describe())


# 전체 결측값 개수 비교
print("\n[전체 결측값 비교]")

print("압축기 결측값:", df_metro_compressor.isna().sum().sum())

print("디지털 신호 결측값:", df_metro_digital.isna().sum().sum())


# ============================================================
# 실습 9. 첫 탐색 종합
# ============================================================

print("\n" + "=" * 60)
print("실습 9. 첫 탐색 종합")
print("=" * 60)

# 12_metro_digital.csv 버전
df = pd.read_csv("data/12_metro_digital.csv")


# 1. head
print("\n[1. head]")
print(df.head())


# 2. shape
print("\n[2. shape]")
print(df.shape)


# 3. columns
print("\n[3. columns]")
print(df.columns)


# 4. dtypes
print("\n[4. dtypes]")
print(df.dtypes)


# 5. info
print("\n[5. info]")
df.info()


# 6. describe
print("\n[6. describe]")
print(df.describe())

# 12_metro_compressoor.csv 버전
df_2 = pd.read_csv("data/12_metro_compressor.csv")


# 1. head
print("\n[1. head]")
print(df_2.head())


# 2. shape
print("\n[2. shape]")
print(df_2.shape)


# 3. columns
print("\n[3. columns]")
print(df_2.columns)


# 4. dtypes
print("\n[4. dtypes]")
print(df_2.dtypes)


# 5. info
print("\n[5. info]")
df_2.info()


# 6. describe
print("\n[6. describe]")
print(df_2.describe())
