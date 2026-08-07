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
    "88.8",
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