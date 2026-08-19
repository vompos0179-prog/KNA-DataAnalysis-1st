import pandas as pd

sensor = pd.read_csv("data/14_equipment_sensor.csv", encoding="utf-8-sig")
qc = pd.read_csv("data/14_hydraulic_qc.csv", encoding="utf-8-sig")

# ==================================================
# 실습 1. 평균·분산·표준편차 구하기
# ==================================================

print("\n========== 실습 1 ==========")

# 진동 전체 평균
진동_평균 = sensor["vibration"].mean()
print("전체 진동 평균")
print(round(진동_평균, 2))

# 진동 전체 분산
진동_분산 = sensor["vibration"].var()
print("\n전체 진동 분산")
print(round(진동_분산, 2))

# 진동 전체 표준편차
진동_표준편차 = sensor["vibration"].std()
print("\n전체 진동 표준편차")
print(round(진동_표준편차, 2))

# 표준편차를 제곱하면 분산과 같은 값이 나옵니다.
표준편차_제곱 = 진동_표준편차**2
print("\n표준편차의 제곱")
print(round(표준편차_제곱, 2))

# 라인별 진동 평균
라인별_진동_평균 = sensor.groupby("line")["vibration"].mean().round(2)
print("\n라인별 진동 평균")
print(라인별_진동_평균)

# 라인별 진동 표준편차
라인별_진동_표준편차 = sensor.groupby("line")["vibration"].std().round(2)
print("\n라인별 진동 표준편차")
print(라인별_진동_표준편차)


# ==================================================
# 실습 2. 그룹별 통계 응용
# ==================================================

print("\n========== 실습 2 ==========")

# 합격·불합격별 지표 평균
검사결과별_평균 = qc.groupby("검사결과").mean().round(2)
print("\n합격·불합격별 지표 평균")
print(검사결과별_평균)

# 합격·불합격별 지표 표준편차
검사결과별_표준편차 = qc.groupby("검사결과").std().round(2)
print("\n합격·불합격별 지표 표준편차")
print(검사결과별_표준편차)


# ==================================================
# 실습 3. agg로 여러 통계 한 번에 구하기
# ==================================================

print("\n========== 실습 3 ==========")

# 교대별 진동의 평균, 표준편차, 최댓값
교대별_진동 = sensor.groupby("shift")["vibration"].agg(["mean", "std", "max"]).round(2)

print("\n교대별 진동 통계")
print(교대별_진동)

# 설비별 평균온도, 평균진동, 측정수
설비별_요약 = (
    sensor.groupby("machine")
    .agg(
        평균온도=("temp", "mean"),
        평균진동=("vibration", "mean"),
        측정수=("temp", "count"),
    )
    .round(2)
)

print("\n설비별 요약")
print(설비별_요약)


# ==================================================
# 실습 4. 설비 진단표 만들기
# ==================================================

print("\n========== 실습 4 ==========")

# 설비별로 여러 통계 구하기
설비_진단표 = (
    sensor.groupby("machine")
    .agg(
        측정수=("temp", "count"),
        평균온도=("temp", "mean"),
        온도편차=("temp", "std"),
        평균진동=("vibration", "mean"),
        평균압력=("pressure", "mean"),
    )
    .round(2)
)

# 온도편차가 큰 순서로 정렬하기
설비_진단표 = 설비_진단표.sort_values("온도편차", ascending=False)

print("\n설비 진단표")
print(설비_진단표)


# ==================================================
# 실습 5. 그룹별 통계량 종합
# ==================================================

print("\n========== 실습 5 ==========")

# 온도 전체 평균
온도_평균 = sensor["temp"].mean()
print("\n전체 온도 평균")
print(round(온도_평균, 2))

# 온도 전체 표준편차
온도_표준편차 = sensor["temp"].std()
print("\n전체 온도 표준편차")
print(round(온도_표준편차, 2))

# 라인별 온도 평균
라인별_온도_평균 = sensor.groupby("line")["temp"].mean().round(2)
print("\n라인별 온도 평균")
print(라인별_온도_평균)

# 라인별 온도 중앙값
라인별_온도_중앙값 = sensor.groupby("line")["temp"].median().round(2)
print("\n라인별 온도 중앙값")
print(라인별_온도_중앙값)

# 실습 4에서 만든 설비 진단표 확인
print("\n온도편차가 큰 순서로 정렬한 최종 설비 진단표")
print(설비_진단표)
