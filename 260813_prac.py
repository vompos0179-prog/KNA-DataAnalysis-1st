import pandas as pd

# CSV 파일 불러오기
df_digital = pd.read_csv("data/12_metro_digital.csv")

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

print("\n" + "=" * 60)
print("실습 6. describe()로 이상 신호 찾기")
print("=" * 60)

# 지하철 공기압축기 데이터 불러오기
df_compressor = pd.read_csv("data/12_metro_compressor.csv")

print("\n[describe()]")
print(df_compressor.describe())

# 75%와 최대값 비교
print("\n[75%와 최대값 비교]")

# 숫자형 열만 선택
numeric_data = df_compressor.select_dtypes(include="number")

for column in numeric_data.columns:

    q75 = numeric_data[column].quantile(0.75)
    max_value = numeric_data[column].max()

    print(
        column,
        "→ 75%:",
        round(q75, 2),
        ", max:",
        round(max_value, 2),
        ", 차이:",
        round(max_value - q75, 2),
    )


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

# 디지털 데이터 불러오기
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


print("\n" + "=" * 60)
print("첫 탐색 완료")
print("=" * 60)
