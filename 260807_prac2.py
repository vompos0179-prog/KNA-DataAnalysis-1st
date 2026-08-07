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

import csv


def read_csv(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as f:

            reader = list(csv.reader(f))

            # 첫 줄은 헤더
            header = reader[0]

            # 나머지는 데이터
            rows = reader[1:]

            return header, rows

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        return [], []


file_path = "data/09_ict_inspection_dirty.csv"

# CSV 읽기
header, rows = read_csv(file_path)

part_dict = {}

for row in rows:

    # 부품명 가져오기
    part = row[1].strip()

    # 부품명이 없으면 건너뛴다.
    if part == "":
        continue

    # 처음 나온 부품이면 빈 리스트 생성
    if part not in part_dict:
        part_dict[part] = []

    # 해당 부품 데이터 저장
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

    # 행의 길이가 부족하면 건너뛴다.
    if len(row) < 7:
        continue

    # 부품명
    part = row[1].strip()

    # 부품명이 없으면 건너뛴다.
    if part == "":
        continue

    if part not in part_dict:
        part_dict[part] = []

    part_dict[part].append(row)


print("===== 부품별 통계 =====")

for part in part_dict:

    values = []

    # 측정값만 저장
    for row in part_dict[part]:

        value = row[2].strip()

        # 결측이나 빈칸은 제외
        if value == "" or value == "결측":
            continue

        try:
            value = float(value)
            values.append(value)

        except ValueError:
            continue

    # 정상 데이터가 없으면 건너뛴다.
    if len(values) == 0:
        continue

    avg = calc_avg(values)
    max_value = calc_max(values)
    min_value = calc_min(values)

    print(f"\n[{part}]")
    print(f"평균 : {avg:.2f}")
    print(f"최대 : {max_value}")
    print(f"최소 : {min_value}")

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

    # 데이터 개수가 부족하면 건너뛴다.
    if len(row) < 7:
        continue

    part = row[1].strip()

    # 부품명이 없으면 건너뛴다.
    if part == "":
        continue

    if part not in part_dict:
        part_dict[part] = []

    part_dict[part].append(row)


print("===== 부품별 통계 =====")

for part in part_dict:

    values = []

    for row in part_dict[part]:

        try:

            # 측정값 가져오기
            value = row[2].strip()

            # 빈 문자열이면 오류 발생
            if value == "":
                raise ValueError("빈 데이터")

            # 숫자로 변환
            value = float(value)

            values.append(value)

        except ValueError:

            print(f"{part} : 잘못된 데이터 -> '{row[2]}'")

            # 다음 데이터 처리
            continue

    # 정상 데이터가 없으면 건너뛴다.
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

    # 데이터 개수가 부족하면 건너뛴다.
    if len(row) < 7:
        continue

    part = row[1].strip()

    # 부품명이 없으면 건너뛴다.
    if part == "":
        continue

    if part not in part_dict:
        part_dict[part] = []

    part_dict[part].append(row)

with open("report.txt", "w", encoding="utf-8") as report:

    report.write("===== 부품별 검사 결과 =====\n\n")

    for part in part_dict:

        values = []

        for row in part_dict[part]:

            try:

                value = row[2].strip()

                # 빈 문자열이면 오류 발생
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

    # 데이터 개수가 부족하면 건너뛴다.
    if len(row) < 7:
        continue

    # 부품명
    part = row[1].strip()

    # 부품명이 없으면 건너뛴다.
    if part == "":
        continue

    if part not in part_dict:
        part_dict[part] = []

    part_dict[part].append(row)


print("===== 부품별 검사 결과 =====")

for part in part_dict:

    values = []

    standard = None
    upper = None
    lower = None

    for row in part_dict[part]:

        try:

            value = row[2].strip()

            # 빈 데이터는 건너뛴다.
            if value == "":
                continue

            value = float(value)
            values.append(value)

            # 기준값은 정상 데이터에서 한 번만 저장
            if standard is None:

                standard = float(row[3])
                upper = float(row[4])
                lower = float(row[5])

        except ValueError:
            continue

    # 정상 데이터가 없으면 건너뛴다.
    if len(values) == 0:
        continue

    avg = calc_avg(values)

    print(f"\n[{part}]")
    print(f"기준값 : {standard}")
    print(f"평균 : {avg:.2f}")

    # 평균과 허용 범위 비교
    if lower <= avg <= upper:
        print("결과 : PASS")
    else:
        print("결과 : FAIL")
