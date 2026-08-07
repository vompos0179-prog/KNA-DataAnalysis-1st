print("===============실습 1. finally로 파일 안전하게 닫기================")

# file = None

# try:
#     file = open("test.txt", "r")

#     print(file.read())

#     # 일부러 오류 발생
#     number = int("abc")

# except ValueError:
#     print("숫자로 변환할 수 없습니다.")

# finally:
#     if file:
#         file.close()
#         print("파일을 안전하게 닫았습니다.")

print("===============실습예제 2================")

# 소수점 이하의 숫자가 포함된 숫자들을 20개정도 만들어 문자로 리스트에 담기
# 그 사이 엉뚱한 글자들이 포함된 내용 추가
# 위 리스트 데이터를 사용해서 문제 풀기

values = [
    "10.5",
    "25.8",
    "abc",
    "30.2",
    "18.7",
    "hello",
    "45.9",
    "12.3",
    "99.1",
    "python",
    "50.5",
    "70.8",
    "error",
    "15.6",
    "80.4",
    "90.2",
    "good",
    "33.3",
    "44.4",
    "55.5",
    "test",
    "66.6",
    "77.7",
    "88.8"
]

total = 0

for value in values:
    try:
        # 문자열을 실수로 변환
        num = float(value)

        # 정상 데이터만 합계에 더하기
        total += num

    except ValueError:
        # 숫자가 아니면 건너뛰기
        continue

print("정상 데이터의 합계 :", round(total, 1))

print("===============실습예제 3================")

# 다음과 같은 식의 리스트를 만들어 반복문으로 처리
# for문으로 리스트의 문자열을 꺼내어 해당 이름의 파일들을 열어보기 시도하면 됨.
# file_names = ["08_press.csv", "09_ict.csv", "09_ict_dirty.csv"]

import os

file_names = ["08_press.csv", "09_ict.csv", "09_ict_dirty.csv"]

count = 0

for file_name in file_names:
    path = os.path.join("data", file_name)

    try:
        with open(path, "r") as file:
            print(file_name, "파일 처리 완료")

        count += 1

    except FileNotFoundError:
        print(file_name, "파일이 없습니다.")
        continue

print("처리한 파일 수 :", count)

print("===============종합 실습================")

print("============1단계=============")

# ==========================================
# 실습 1단계 - CSV 읽기
# ==========================================

# csv 모듈 사용
import csv


# CSV 파일을 읽는 함수
def read_csv(file_path):

    try:
        # CSV 파일 열기
        with open(file_path, "r", encoding="utf-8") as f:

            # csv 데이터를 리스트로 저장
            reader = list(csv.reader(f))

            # 첫 번째 줄은 헤더
            header = reader[0]

            # 두 번째 줄부터는 데이터
            rows = reader[1:]

            # 헤더 출력
            print("헤더")
            print(header)

            print()

            # 데이터 개수 출력
            print("데이터 행 수 :", len(rows))

            # 다음 단계에서 사용할 수 있도록 반환
            return header, rows

    # 파일이 없는 경우
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

        # 빈 헤더와 빈 데이터 반환
        return [], []


file_path = "data/09_ict_inspection_dirty.csv"

header, rows = read_csv(file_path)

print("============2단계=============")

# csv 모듈 사용
import csv

def read_csv(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as f:

            reader = list(csv.reader(f))

            header = reader[0]
            rows = reader[1:]

            return header, rows

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        return [], []

file_path = "data/09_ict_inspection_dirty.csv"

# 헤더와 데이터 읽기
header, rows = read_csv(file_path)


# ------------------------------------------
# 부품별 데이터를 저장할 딕셔너리
# key : 부품명
# value : 해당 부품의 데이터(리스트)
# ------------------------------------------
part_dict = {}

for row in rows:

    # 부품명(E2, F2 ...)
    part = row[1]

    # 처음 나온 부품이면 빈 리스트 생성
    if part not in part_dict:
        part_dict[part] = []

    # 해당 부품 리스트에 데이터 추가
    part_dict[part].append(row)


print("===== 부품별 데이터 개수 =====")

for part in part_dict:

    print(f"{part} : {len(part_dict[part])}개")

print("============3단계=============")

import csv

def read_csv(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as f:

            reader = list(csv.reader(f))

            header = reader[0]
            rows = reader[1:]

            return header, rows

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        return [], []

def calc_avg(values):

    total = 0

    for value in values:
        total += value

    avg = total / len(values)

    return avg

def calc_max(values):

    max_value = values[0]

    for value in values:

        if value > max_value:
            max_value = value

    return max_value

def calc_min(values):

    min_value = values[0]

    for value in values:

        if value < min_value:
            min_value = value

    return min_value

file_path = "data/09_ict_inspection_dirty.csv"

header, rows = read_csv(file_path)


# 부품별 데이터 저장
part_dict = {}

for row in rows:

    part = row[1]

    if part not in part_dict:
        part_dict[part] = []

    part_dict[part].append(row)


print("===== 부품별 통계 =====")

# 부품별 평균, 최대, 최소 출력
for part in part_dict:

    values = []

    # 측정값만 리스트에 저장
    for row in part_dict[part]:

        value = float(row[2])
        values.append(value)

    avg = calc_avg(values)
    max_value = calc_max(values)
    min_value = calc_min(values)

    print(f"{part}")
    print(f"평균 : {avg:.2f}")
    print(f"최대 : {max_value}")
    print(f"최소 : {min_value}")
    print()

print("============4단계=============")

import csv

def read_csv(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as f:

            reader = list(csv.reader(f))

            header = reader[0]
            rows = reader[1:]

            return header, rows

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        return [], []

def calc_avg(values):

    total = 0

    for value in values:
        total += value

    return total / len(values)

def calc_max(values):

    max_value = values[0]

    for value in values:

        if value > max_value:
            max_value = value

    return max_value

def calc_min(values):

    min_value = values[0]

    for value in values:

        if value < min_value:
            min_value = value

    return min_value

file_path = "data/09_ict_inspection_dirty.csv"

header, rows = read_csv(file_path)

# 부품별 데이터 저장
part_dict = {}

for row in rows:

    part = row[1]

    if part not in part_dict:
        part_dict[part] = []

    part_dict[part].append(row)


print("===== 부품별 통계 =====")

for part in part_dict:

    values = []

    for row in part_dict[part]:

        try:

            # 측정값
            value = row[2]

            # 빈 문자열이면 오류 발생
            if value == "":
                raise ValueError("빈 데이터")

            # 숫자로 변환
            value = float(value)

            values.append(value)

        except ValueError:

            print(f"{part} : 잘못된 데이터 -> {row[2]}")

            # 다음 데이터 처리
            continue

    # 정상 데이터가 하나도 없으면 건너뜀
    if len(values) == 0:
        continue

    avg = calc_avg(values)
    max_value = calc_max(values)
    min_value = calc_min(values)

    print()
    print(f"[{part}]")
    print(f"평균 : {avg:.2f}")
    print(f"최대 : {max_value}")
    print(f"최소 : {min_value}")

print("============5단계=============")

import csv

def read_csv(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as f:

            reader = list(csv.reader(f))

            header = reader[0]
            rows = reader[1:]

            return header, rows

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        return [], []

def calc_avg(values):

    total = 0

    for value in values:
        total += value

    return total / len(values)

def calc_max(values):

    max_value = values[0]

    for value in values:

        if value > max_value:
            max_value = value

    return max_value

def calc_min(values):

    min_value = values[0]

    for value in values:

        if value < min_value:
            min_value = value

    return min_value

file_path = "data/09_ict_inspection_dirty.csv"

header, rows = read_csv(file_path)

# 부품별 데이터 저장
part_dict = {}

for row in rows:

    part = row[1]

    if part not in part_dict:
        part_dict[part] = []

    part_dict[part].append(row)

with open("report.txt", "w", encoding="utf-8") as report:

    report.write("===== 부품별 검사 결과 =====\n\n")

    for part in part_dict:

        values = []

        for row in part_dict[part]:

            try:

                value = row[2]

                if value == "":
                    raise ValueError("빈 데이터")

                value = float(value)

                values.append(value)

            except ValueError:
                continue

        # 정상 데이터가 없으면 건너뜀
        if len(values) == 0:
            continue

        avg = calc_avg(values)
        max_value = calc_max(values)
        min_value = calc_min(values)

        report.write(f"[{part}]\n")
        report.write(f"평균 : {avg:.2f}\n")
        report.write(f"최대 : {max_value}\n")
        report.write(f"최소 : {min_value}\n")
        report.write("\n")

print("report.txt 파일 저장 완료!")

print("============6단계=============")

import csv

def read_csv(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as f:

            reader = list(csv.reader(f))

            header = reader[0]
            rows = reader[1:]

            return header, rows

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        return [], []

def calc_avg(values):

    total = 0

    for value in values:
        total += value

    return total / len(values)

file_path = "data/09_ict_inspection_dirty.csv"

header, rows = read_csv(file_path)

# 부품별 데이터 저장
part_dict = {}

for row in rows:

    part = row[1]

    if part not in part_dict:
        part_dict[part] = []

    part_dict[part].append(row)


print("===== 부품별 통계 검증 =====")

# 부품별 평균과 기준값 비교
for part in part_dict:

    values = []

    # 첫 번째 행에서 기준값, 상한치, 하한치 가져오기
    standard = float(part_dict[part][0][3])
    upper = float(part_dict[part][0][4])
    lower = float(part_dict[part][0][5])

    for row in part_dict[part]:

        try:

            value = row[2]

            if value == "":
                raise ValueError("빈 데이터")

            value = float(value)

            values.append(value)

        except ValueError:
            continue

    # 정상 데이터가 없으면 다음 부품으로
    if len(values) == 0:
        continue

    avg = calc_avg(values)

    print(f"\n[{part}]")
    print(f"기준값 : {standard}")
    print(f"평균 : {avg:.2f}")

    # 평균이 허용 범위 안에 있는지 검사
    if lower <= avg <= upper:
        print("결과 : PASS")
    else:
        print("결과 : FAIL")