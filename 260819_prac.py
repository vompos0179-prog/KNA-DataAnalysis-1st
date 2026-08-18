import pandas as pd

df = pd.read_csv("data/14_equipment_sensor.csv", encoding="utf-8-sig")

qc = pd.read_csv("data/14_hydraulic_qc.csv", encoding="utf-8-sig")


# ==================================================
# 실습 4. groupby로 그룹 집계하기
# ==================================================

print("\n[실습 4] groupby로 그룹 집계")

# line을 기준으로 그룹을 나누고 pressure의 평균 구하기
print("\n라인별 평균 압력")
print(df.groupby("line")["pressure"].mean().round(2))

# machine을 기준으로 그룹을 나누고 temp의 최댓값 구하기
print("\n설비별 최고 온도")
print(df.groupby("machine")["temp"].max())

# shift를 기준으로 그룹을 나누고 각 그룹의 행 개수 세기
print("\n교대별 측정 건수")
print(df.groupby("shift").size())


# ==================================================
# 실습 5. 그룹별 평균을 구하고 정렬하기
# ==================================================

print("\n[실습 5] 그룹별 평균 비교와 정렬")

# 설비별 진동 평균 구하기
설비별_진동평균 = df.groupby("machine")["vibration"].mean()

# 평균이 큰 설비부터 내림차순으로 정렬하기
print("\n진동 평균이 큰 설비 순서")
print(설비별_진동평균.sort_values(ascending=False).round(3))

# 실제 결과: M01의 진동 평균이 가장 큽니다.


# ==================================================
# 실습 6. 여러 기준을 조합하여 그룹 만들기
# ==================================================

print("\n[실습 6] 여러 기준 조합 그룹")

# line과 shift를 함께 기준으로 묶고 진동 평균 구하기
print("\n라인×교대별 진동 평균")
print(df.groupby(["line", "shift"])["vibration"].mean().round(3))

# 같은 두 기준으로 각 그룹의 측정 건수 세기
print("\n라인×교대별 측정 건수")
print(df.groupby(["line", "shift"]).size())


# ==================================================
# 실습 7. 빈도와 그룹 집계 종합
# ==================================================

print("\n[실습 7] 빈도와 그룹 집계 종합")

# 1. 설비 구성 확인
print("\n설비 구성")
print(df["machine"].value_counts())

# 2. 정상과 고장의 비율 확인
print("\n정상·고장 비율")
print(df["result"].value_counts(normalize=True).round(3))

# 3. result가 고장인 행만 골라내기
고장데이터 = df[df["result"] == "고장"]

# 고장 데이터에서 라인별 고장 건수 세기
print("\n라인별 고장 건수")
print(고장데이터.groupby("line").size())

# 4. 설비별 온도와 진동의 평균을 함께 구하기
# 열을 여러 개 고를 때는 대괄호를 두 번 사용합니다.
print("\n설비별 온도·진동 평균")
print(df.groupby("machine")[["temp", "vibration"]].mean().round(2))


# ==================================================
# 종합 산출물 - 결과를 세 문장으로 정리
# ==================================================

print("\n[종합 산출물]")
print("1. 전체 빈도에서 QC 불합격은 전체의 약 6%라는 것을 알 수 있습니다.")
print("2. 그룹 비교에서 M01 설비의 진동 평균이 가장 높다는 것을 알 수 있습니다.")
print("3. B라인 야간 그룹의 진동 평균이 가장 높아 추가 확인이 필요합니다.")
