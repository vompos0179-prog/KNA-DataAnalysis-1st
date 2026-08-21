import pandas as pd

df1 = pd.read_csv("data/15_01_사출성형_공정.csv")
df2 = pd.read_csv("data/15_02_사출성형_공정.csv")
log_df = pd.read_csv("data/15_사출성형_로그.csv")


# --------------------------------------------------
# 실습 1. dropna로 행·열 삭제
# --------------------------------------------------
print("\n[실습 1] dropna로 행·열 삭제")

# 원본 데이터 크기 확인
print("원본 크기:", df1.shape)

# 결측치가 하나라도 있는 행 삭제
row_deleted = df1.dropna()
print("행 삭제 후 크기:", row_deleted.shape)

# 결측치가 하나라도 있는 열 삭제
column_deleted = df1.dropna(axis=1)
print("열 삭제 후 크기:", column_deleted.shape)

# 예상 결과
# 원본: (250, 22)
# 행 삭제: (76, 22)
# 열 삭제: (250, 10)


# --------------------------------------------------
# 실습 2. dropna 옵션 조절
# --------------------------------------------------
print("\n[실습 2] dropna 옵션 조절")

# 모든 값이 결측치인 행만 삭제
all_missing_deleted = df1.dropna(how="all")
print("모든 값이 비어 있는 행 삭제 후:", all_missing_deleted.shape)

# 값이 20개 이상 들어 있는 행만 남기기
thresh_result = df1.dropna(thresh=20)
print("값이 20개 이상인 행만 남긴 후:", thresh_result.shape)

# '사출압력'이 결측치인 행만 삭제
subset_result = df1.dropna(subset=["사출압력"])
print("사출압력이 비어 있는 행 삭제 후:", subset_result.shape)

# 예상 결과
# 모든 값이 비어 있는 행 삭제: (250, 22)
# thresh=20 적용: (162, 22)
# 사출압력 기준 삭제: (249, 22)


# --------------------------------------------------
# 실습 3. 결측 비율 기준 컬럼 제거
# --------------------------------------------------
print("\n[실습 3] 결측 비율 기준 컬럼 제거")

# 열별 결측 비율 계산
missing_ratio = df1.isna().mean() * 100
print("열별 결측 비율(%)")
print(missing_ratio.round(1))

# 결측 비율이 40%를 초과하는 열 찾기
high_missing_columns = missing_ratio[missing_ratio > 40].index
print("제거할 열:", list(high_missing_columns))

# 결측 비율이 높은 열 제거
ratio_result = df1.drop(columns=high_missing_columns)
print("열 제거 후 크기:", ratio_result.shape)

# 예상 결과
# 제거할 열: ['계량종료점', '감압시간']
# 열 제거 후 크기: (250, 20)


# --------------------------------------------------
# 실습 4. 삭제 손실 비교
# --------------------------------------------------
print("\n[실습 4] 삭제 손실 비교")

original_rows = len(df1)
dropna_rows = len(df1.dropna())
thresh_rows = len(df1.dropna(thresh=20))

comparison_table = pd.DataFrame(
    {
        "처리방법": ["원본", "결측 행 삭제", "thresh=20"],
        "남은 행 수": [original_rows, dropna_rows, thresh_rows],
    }
)

# 원본 행 수와 비교하여 손실률 계산
comparison_table["손실률(%)"] = (
    (original_rows - comparison_table["남은 행 수"]) / original_rows * 100
).round(1)

print(comparison_table)

# 예상 결과
# 원본 손실률: 0.0%
# 결측 행 삭제 손실률: 69.6%
# thresh=20 손실률: 35.2%


# --------------------------------------------------
# 실습 5. fillna 평균·중앙값 대체
# --------------------------------------------------
print("\n[실습 5] fillna 평균·중앙값 대체")

# PDF의 '센서17'에 해당하는 실제 열로 스크루속도를 사용
mean_value = df1["스크루속도"].mean()
median_value = df1["스크루속도"].median()

print("스크루속도 평균:", round(mean_value, 2))
print("스크루속도 중앙값:", round(median_value, 2))

# 평균으로 결측치 채우기
mean_filled = df1.copy()
mean_filled["스크루속도"] = mean_filled["스크루속도"].fillna(mean_value)

# 중앙값으로 결측치 채우기
median_filled = df1.copy()
median_filled["스크루속도"] = median_filled["스크루속도"].fillna(median_value)

print("평균 대체 후 남은 결측:", mean_filled["스크루속도"].isna().sum())
print("중앙값 대체 후 남은 결측:", median_filled["스크루속도"].isna().sum())

# 예상 결과
# 평균: 약 46.89
# 중앙값: 약 47.42
# 두 방법 모두 스크루속도의 남은 결측: 0


# --------------------------------------------------
# 실습 6. 최빈값·앞뒤 값 대체
# --------------------------------------------------
print("\n[실습 6] 최빈값·앞뒤 값 대체")

log_result = log_df.copy()

# 사출기의 최빈값 구하기
machine_mode = log_result["사출기"].mode()[0]
print("사출기 최빈값:", machine_mode)

# 사출기의 결측치를 최빈값으로 채우기
log_result["사출기"] = log_result["사출기"].fillna(machine_mode)

# 측정시각을 날짜·시간 형식으로 바꾸고 시간순으로 정렬
log_result["측정시각"] = pd.to_datetime(log_result["측정시각"])
log_result = log_result.sort_values("측정시각")

# 배럴온도의 결측치를 앞의 값으로 먼저 채우고,
# 맨 앞에 결측치가 남으면 뒤의 값으로 채우기
log_result["배럴온도"] = log_result["배럴온도"].ffill().bfill()

print("사출기의 남은 결측:", log_result["사출기"].isna().sum())
print("배럴온도의 남은 결측:", log_result["배럴온도"].isna().sum())

# 예상 결과
# 사출기 최빈값: 1호기
# 사출기와 배럴온도의 남은 결측: 0


# --------------------------------------------------
# 실습 7. 그룹별 대체
# --------------------------------------------------
print("\n[실습 7] 그룹별 대체")

group_result = df2.copy()

# 사출기별 스크루속도 평균으로 결측치 채우기
group_result["스크루속도"] = group_result.groupby("사출기")["스크루속도"].transform(
    lambda group: group.fillna(group.mean())
)

# 나머지 숫자형 열의 결측치는 각 열의 전체 중앙값으로 채우기
numeric_columns = group_result.select_dtypes(include="number").columns

for column in numeric_columns:
    median_value = group_result[column].median()
    group_result[column] = group_result[column].fillna(median_value)

print("처리 후 전체 결측 개수:", group_result.isna().sum().sum())

# 예상 결과
# 스크루속도는 사출기별 평균으로 대체
# 나머지 숫자형 결측치는 중앙값으로 대체
# 처리 후 전체 결측 개수: 0


# --------------------------------------------------
# 실습 8. 제거 vs 대체 비교
# --------------------------------------------------
print("\n[실습 8] 제거 vs 대체 비교")

# 결측 비율이 40%를 초과하는 열을 먼저 제거
missing_ratio = df1.isna().mean() * 100
high_missing_columns = missing_ratio[missing_ratio > 40].index
base_data = df1.drop(columns=high_missing_columns)

# 제거 버전: 결측치가 있는 행 삭제
remove_version = base_data.dropna()

# 대체 버전: 숫자형 결측치를 중앙값으로 채우기
replace_version = base_data.copy()
numeric_columns = replace_version.select_dtypes(include="number").columns

for column in numeric_columns:
    median_value = replace_version[column].median()
    replace_version[column] = replace_version[column].fillna(median_value)

print("기준 데이터 행 수:", len(base_data))
print("제거 버전 행 수:", len(remove_version))
print("대체 버전 행 수:", len(replace_version))
print("대체 버전의 남은 결측:", replace_version.isna().sum().sum())

# 예상 결과
# 기준 데이터: 250행
# 제거 버전: 110행
# 대체 버전: 250행
# 대체 버전의 남은 결측: 0


# --------------------------------------------------
# 실습 9. 두 데이터 종합 처리 후 저장
# --------------------------------------------------
print("\n[실습 9] 두 데이터 종합 처리 후 저장")

# 15_01 데이터 처리
missing_ratio1 = df1.isna().mean() * 100
remove_columns1 = missing_ratio1[missing_ratio1 > 40].index
final_df1 = df1.drop(columns=remove_columns1)

numeric_columns1 = final_df1.select_dtypes(include="number").columns

for column in numeric_columns1:
    median_value = final_df1[column].median()
    final_df1[column] = final_df1[column].fillna(median_value)

print("15_01 처리 후 크기:", final_df1.shape)
print("15_01 처리 후 남은 결측:", final_df1.isna().sum().sum())

# 15_02 데이터 처리
missing_ratio2 = df2.isna().mean() * 100
remove_columns2 = missing_ratio2[missing_ratio2 > 40].index
final_df2 = df2.drop(columns=remove_columns2)

numeric_columns2 = final_df2.select_dtypes(include="number").columns

for column in numeric_columns2:
    median_value = final_df2[column].median()
    final_df2[column] = final_df2[column].fillna(median_value)

print("15_02 처리 후 크기:", final_df2.shape)
print("15_02 처리 후 남은 결측:", final_df2.isna().sum().sum())

# 처리한 데이터를 새 CSV 파일로 저장
# index=False는 CSV에 불필요한 행 번호가 저장되지 않게 함
final_df1.to_csv(
    "data/15_01_사출성형_공정_처리완료.csv", index=False, encoding="utf-8-sig"
)

final_df2.to_csv(
    "data/15_02_사출성형_공정_처리완료.csv", index=False, encoding="utf-8-sig"
)

print("처리 완료 CSV 파일 2개를 data 폴더에 저장했습니다.")

# 예상 결과
# 15_01: (250, 20), 남은 결측 0
# 15_02: (250, 20), 남은 결측 0
