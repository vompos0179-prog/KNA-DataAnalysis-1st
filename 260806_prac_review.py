print("===============실습 1================")
# sample.txt 파일을 읽기 모드로 열기
f = open("sample.txt", "r", encoding="utf-8")

# 파일 전체를 하나의 문자열로 읽기
text = f.read()

# 읽은 내용 출력
print(text)

# 파일 닫기
f.close()

# 다시 파일 열기
f = open("sample.txt", "r", encoding="utf-8")

# 모든 줄을 리스트 형태로 읽기
lines = f.readlines()

# 리스트 출력
print(lines)

# 파일 닫기
f.close()

print("===============실습 2================")

# memo.txt 파일을 쓰기 모드로 열기
with open("memo.txt", "w", encoding="utf-8") as f:

    # 첫 번째 줄 작성
    f.write("안녕하세요.\n")

    # 두 번째 줄 작성
    f.write("파일 쓰기 실습입니다.\n")

# 읽기 모드로 다시 열기
with open("memo.txt", "r", encoding="utf-8") as f:

    # 저장된 내용 출력
    print(f.read())

print("===============실습 3================")

# memo.txt 파일을 추가 모드로 열기
with open("memo.txt", "a", encoding="utf-8") as f:

    # 기존 내용 뒤에 추가
    f.write("추가된 내용입니다.\n")

# 파일 내용 확인
with open("memo.txt", "r", encoding="utf-8") as f:
    print(f.read())

print("===============실습 4================")

# csv 모듈 불러오기
import csv

# CSV 파일 열기
with open("data/08_press.csv", "r", encoding="utf-8") as f:

    # reader 객체 만들기
    reader = csv.reader(f)

    # 한 행 씩 읽어서 출력
    for row in reader:
        print(row)

print("===============실습 5================")

# csv 모듈 불러오기
import csv

# result.csv 파일 생성
with open("result.csv", "w", encoding="utf-8", newline="") as f:

    # writer 객체 만들기
    writer = csv.writer(f)

    # 헤더 작성
    writer.writerow(["이름", "점수"])

    # 데이터 작성
    writer.writerow(["홍길동", 90])
    writer.writerow(["김철수", 85])

print("===============실습 6================")

# csv 모듈 불러오기
import csv

# 조건을 만족하는 데이터를 저장할 리스트
result = []

# CSV 파일 열기
with open("data/08_press.csv", "r", encoding="utf-8") as f:

    # reader 객체 생성
    reader = csv.reader(f)

    # 첫 번째 줄(헤더) 저장
    header = next(reader)

    # 데이터 한 줄씩 반복
    for row in reader:

        # 전류 값을 실수형으로 변환
        current = float(row[4])

        # 전류가 90보다 크면 리스트에 저장
        if current > 90:
            result.append(row)

# 결과를 새 CSV 파일로 저장
with open("high_current.csv", "w", encoding="utf-8", newline="") as f:

    # writer 객체 생성
    writer = csv.writer(f)

    # 헤더 저장
    writer.writerow(header)

    # 조건을 만족한 데이터 저장
    writer.writerows(result)