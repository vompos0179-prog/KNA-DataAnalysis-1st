import pandas as pd

df = pd.read_csv("data/14_equipment_sensor.csv", encoding="utf-8-sig")

qc = pd.read_csv("data/14_hydraulic_qc.csv", encoding="utf-8-sig")


# ==================================================
# 실습 1. value_counts로 빈도 세기
# ==================================================

print("\n[실습 1] value_counts로 빈도 세기")

# 데이터의 앞부분 5행 확인
print("\n설비 데이터 앞부분")
print(df.head())

# 데이터의 행 개수, 열 이름, 자료형 확인
print("\n설비 데이터 구조")
df.info()

# machine 열의 값별 개수 세기
print("\n설비별 빈도")
print(df["machine"].value_counts())

# shift 열의 값별 개수 세기
print("\n교대별 빈도")
print(df["shift"].value_counts())

# 실제 결과: M04가 42건으로 가장 많습니다.


# ==================================================
# 실습 2. 비율과 불균형 데이터
# ==================================================

print("\n[실습 2] 비율과 불균형 데이터")

# 검사결과 열의 합격과 불합격 개수 세기
print("\n합격·불합격 빈도")
print(qc["검사결과"].value_counts())

# normalize=True를 사용하면 개수가 아닌 비율이 나옵니다.
# round(3)은 소수점 셋째 자리까지 표시합니다.
print("\n합격·불합격 비율")
print(qc["검사결과"].value_counts(normalize=True).round(3))

# 실제 결과: 합격 0.940, 불합격 0.060입니다.
# 불합격은 전체의 약 6%이므로 불균형 데이터입니다.


# ==================================================
# 실습 3. pd.cut으로 구간을 만들어 빈도 세기
# ==================================================

print("\n[실습 3] 구간으로 묶어 세기")

# 진동 값의 최솟값과 최댓값 확인
print("\n진동 최솟값")
print(df["vibration"].min())

print("\n진동 최댓값")
print(df["vibration"].max())

# 진동 값을 약함, 보통, 강함의 세 구간으로 나누기
# 경계값 4개를 사용하면 구간은 3개가 만들어집니다.
진동구간 = pd.cut(
    df["vibration"], bins=[0, 2.5, 3.5, 10], labels=["약함", "보통", "강함"]
)

# 만들어진 구간별 개수 세기
print("\n진동 구간별 빈도")
print(진동구간.value_counts(sort=False))

# 실제 결과: 약함 36건, 보통 43건, 강함 41건입니다.


