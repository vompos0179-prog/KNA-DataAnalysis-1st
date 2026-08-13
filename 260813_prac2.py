import pandas as pd

# 0. read_csv로 설비 센서 파일 불러오기
df = pd.read_csv("data/13_diecasting_small.csv")

print("=" * 60)
print("실습 1. 데이터 불러오기와 구조 확인하기")
print("=" * 60)


# 1. head로 앞부분, shape로 행·열 크기 확인
print("--- 앞부분 5행 ---")
print(df.head())

print("\n--- 행·열 크기 (shape) ---")
print(df.shape)  # 예상 결과: (30, 7)

# 2. columns로 열 이름 목록 확인
print("\n--- 열 이름 목록 ---")
print(df.columns)


print("=" * 60)
print("실습 2. 열 선택하기")
print("=" * 60)

# 1. 대괄호 한 겹으로 단일 열을 Series로 선택
형체력_series = df["형체력"]
print("--- 단일 열 (Series) ---")
print(type(형체력_series))
print(형체력_series.head())

# 2. 대괄호 두 겹으로 복수 열을 DataFrame으로 선택
두열_df = df[["형체력", "실린더압력"]]
print("\n--- 복수 열 (DataFrame) ---")
print(type(두열_df))
print(두열_df.head())

# 3. 선택한 열에 mean으로 평균 계산
형체력_평균 = df["형체력"].mean()
print("\n--- 형체력 평균 ---")
print(형체력_평균)


print("=" * 60)
print("실습 3. 공정 센서 열 골라내기")
print("=" * 60)

# 1. 주조 로그 파일 불러오기
df_log = pd.read_csv("data/13_diecasting_small.csv")  # 또는 실습용 주조 로그 CSV 경로

# 2. 한 센서 열을 Series로 선택
sensor_series = df_log["형체력"]
print("--- 한 센서 열 (Series) ---")
print(type(sensor_series))

# 3. 여러 feature 열을 DataFrame으로 선택해 형태 확인
feature_df = df_log[["실린더압력", "주조압력", "형체력"]]
print("\n--- 여러 feature 열 크기 ---")
print(feature_df.shape)  # 예상 결과: (100, 3) 등


print("=" * 60)
print("실습 4. loc와 iloc로 행 선택하기")
print("=" * 60)

# 1. loc로 라벨 기준 단일 행 선택
row_loc = df.loc[0]
print("--- loc[0] 단일 행 (품질등급 확인) ---")
print(row_loc["품질등급"])

# 2. iloc로 번호 기준 단일 행 선택
row_iloc = df.iloc[0]
print("\n--- iloc[0] 단일 행 ---")
print(row_iloc["품질등급"])

# 3. 범위 선택으로 loc(끝 포함)과 iloc(끝 제외) 차이 확인
loc_range = df.loc[0:2]  # 0, 1, 2번 행 (총 3줄)
iloc_range = df.iloc[0:2]  # 0, 1번 행 (총 2줄)

print("\n--- loc[0:2] 줄 수 ---")
print(len(loc_range))  # 출력: 3

print("\n--- iloc[0:2] 줄 수 ---")
print(len(iloc_range))  # 출력: 2


print("=" * 60)
print("실습 5. loc·iloc로 행·열 동시 선택하기")
print("=" * 60)

# 1. loc로 행 범위와 열 이름을 함께 지정 (예: 5행, 2열 범위)
sub1 = df.loc[0:4, ["품질등급", "형체력"]]
print("--- loc 행·열 지정 크기 ---")
print(sub1.shape)  # 예상 결과: (5, 2)

# 2. 다른 행 범위에서 세 열 선택
sub2 = df.loc[0:4, ["품질등급", "형체력", "실린더압력"]]
print("\n--- loc 다른 행 범위 세 열 크기 ---")
print(sub2.shape)  # 예상 결과: (5, 3)

# 3. iloc 음수 인덱스로 마지막 행(또는 마지막 3행) 선택
last_3_rows = df.iloc[-3:]
print("\n--- iloc 마지막 3행 ---")
print(last_3_rows)


print("=" * 60)
print("실습 6. 특정 구간 추출 종합")
print("=" * 60)

# 1. 여러 feature 열을 선택한 뒤 iloc로 앞 구간 추출
extracted1 = df[["실린더압력", "주조압력", "형체력", "비스킷두께", "사이클타임"]].iloc[
    0:10
]
print("--- 실습 6-1 크기 ---")
print(extracted1.shape)  # 예상 결과: (10, 5)

# 2. loc 라벨 범위로 두 열 구간 추출
extracted2 = df.loc[0:10, ["형체력", "실린더압력"]]
print("\n--- 실습 6-2 크기 ---")
print(extracted2.shape)  # loc 0:10은 11행 포함 -> (11, 2)

# 3. iloc 위치 범위로 앞쪽 열 구간 추출
extracted3 = df.iloc[0:10, 0:6]
print("\n--- 실습 6-3 크기 ---")
print(extracted3.shape)  # 예상 결과: (10, 6)
