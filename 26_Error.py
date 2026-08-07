# "================================================="
print("===============try, except================")

# try-except 문
# error 발생 가능성이 있는 코드를 먼저 try와 except 로 실패 가능성을 염두해두고 실행하는 코드
# 실패 예상 지점에 except 코드를 넣어 대처 방안을 넣어두면 실패해도 해당 코드를 실행은 해본다.

# 기본 구조
try:
    temp = int("스물")
except:
    print("못바꿈")

# "================================================="
print("===============else, finally================")

# text = "24.5" # 정상
text = "영크크"  # 비정상

temp = 0

try:
    temp = float(text)
except ValueError:
    print("ValueError 문제가 발생했습니다")
except NameError:
    print("NameError 문제가 발생했습니다")
finally:
    # 오류가 있건 없건 finally의 코드를 실행하 마무리
    print(temp * 2)

# "================================================="
print("===============continue================")

my_list = ["123", "456", "32", "53"]

for text in my_list:
    my_number = int(text)
    print(my_number * 2)
## 혹시라도 리스트 내부에 어떤 문제가 있다고 가정하면, 문제가 있는 지점 이전에는 정상출력 한다.
# 따라서 문제점만 따로 건너뛰고 이어서 진행을 할려고 하면, try-except를 쓰면 된다.

my_list = ["123", "456", "문자열", "32", "53"]

for text in my_list:
    try:
        my_number = int(text)
    except:
        print("문제발생")
        # 문제가 발생했다면, 해당 지점의 실행을 멈추고, 다음 내용을 실행하기(continue)
        continue
    print(my_number)

# 리스트 내부의 문제 발생시 해당 개수 체크 해보기

my_list = ["123", "456", "문자열", "32", "53"]

problems = 0

for text in my_list:
    try:
        my_number = int(text)
    except:
        # print("문제발생")
        # 문제가 발생했다면, 해당 지점의 실행을 멈추고, 다음 내용을 실행하기(continue)
        problems += 1

        continue

    print(my_number)

print(f"{problems} 개는 문제가 있어 skip함.")


print("===============종합 실습예제================")

## 각 학생 별 합계와 평균 점수를 내는 코드

# 필요한 모듈 접근
# 각 학생 별 평균 점수와 전체 평균, 최고 평균 학생, 최저 평균 학생,
# 과목별 평균을 구하는 코드

# 필요한 모듈 접근
import os
import sys
import csv

total_all = 0
student_count = 0

# 최고 평균 학생
max_avg = -1
max_name = ""

# 최저 평균 학생
min_avg = 101
min_name = ""

# 과목별 총점
sum_kor = 0
sum_eng = 0
sum_math = 0

# 파일을 연다
file_path = os.path.join("data", "student_scores.csv")

if not os.path.exists(file_path):
    print("파일을 찾지 못했습니다.")
    sys.exit(1)

with open(file_path, "r", encoding="utf-8") as f:

    # 파일 내용을 리스트화
    reader = csv.DictReader(f)

    for row in reader:
        name = row.get("\ufeff이름", "(이름없음)")

        kor = int(row.get("국어", "0"))
        eng = int(row.get("영어", "0"))
        math = int(row.get("수학", "0"))

        # 학생 평균 계산
        total = (kor + eng + math) / 3

        print(f"{name} | {kor} | {eng} | {math} | {total:.1f}")

        # 최고 평균 학생
        if total > max_avg:
            max_avg = total
            max_name = name

        # 최저 평균 학생
        if total < min_avg:
            min_avg = total
            min_name = name

        # 과목별 총점
        sum_kor += kor
        sum_eng += eng
        sum_math += math

        # 전체 평균 계산
        student_count += 1
        total_all += total

# 전체 평균
avg_all = total_all / student_count

# 과목별 평균
avg_kor = sum_kor / student_count
avg_eng = sum_eng / student_count
avg_math = sum_math / student_count

# 결과 출력

print(f"전체 {student_count}명 | 평균 {avg_all:.1f}점")


print("===== 최고/최저 평균 학생 =====")
print(
    f"최고 평균 학생 : {max_name} ({max_avg:.1f}점) , 최저 평균 학생 : {min_name} ({min_avg:.1f}점)"
)

print("===== 과목별 평균 =====")
print(f"국어 : {avg_kor:.1f}점, 영어 : {avg_eng:.1f}점, 수학 : {avg_math:.1f}점")
