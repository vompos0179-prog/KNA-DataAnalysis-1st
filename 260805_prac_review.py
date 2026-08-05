print("===============실습 1================")
# 모듈을 가져오는 3가지 방법 알아보기

# 방법 1 : import 모듈명
# 모듈명.기능명() 형태로 사용
import math

res1 = math.sqrt(16)  # math 모듈의 sqrt(제곱근) 기능 사용


# 방법 2 : from 모듈 import 기능
# 필요한 기능만 가져와서 모듈명 없이 바로 사용 가능
from math import sqrt

res2 = sqrt(16)


# 방법 3 : import 모듈명 as 별명
# 모듈 이름을 짧게 줄여서 사용 가능
import math as m

res3 = m.sqrt(16)


# 세 가지 방법 모두 같은 결과인지 확인
print(res1)
print(res2)
print(res3)


print("===============실습 2================")
# random과 math 모듈을 이용해 가상의 센서값 만들기


import random

# random.randint(시작값, 끝값)
# 1부터 100 사이의 랜덤한 정수 생성
sensor_value = random.randint(1, 100)

print(f"생성된 센서값: {sensor_value}")


# math.sqrt()
# 숫자의 제곱근 계산
processed_value = math.sqrt(sensor_value)

print(f"가공된 값(제곱근): {processed_value}")

# 실행할 때마다 랜덤 값이 생성되므로 결과가 달라짐


print("===============실습 3================")
# os 모듈을 이용해 현재 폴더의 파일 목록 확인하기


import os

# os.getcwd()
# 현재 파이썬이 실행되는 작업 위치 확인
current_path = os.getcwd()

print(f"현재 작업 경로: {current_path}")


# os.listdir()
# 괄호 안의 경로에 있는 파일과 폴더 목록 가져오기
# "." 은 현재 작업 폴더를 의미
file_list = os.listdir(".")


print("\n--- 전체 파일 목록 ---")

# for문으로 파일 목록 하나씩 출력
for name in file_list:
    print(name)


print("\n--- CSV 파일만 출력 ---")

# .csv로 끝나는 파일만 골라내기
for name in file_list:
    if name.endswith(".csv"):
        print(name)


print("===============실습 4================")
# os를 이용해 특정 파일이 존재하는지 확인하기


# os.path.join()
# 폴더명과 파일명을 연결해서 하나의 경로 생성
target_path = os.path.join("data", "08_press.csv")


# os.path.exists()
# 해당 경로의 파일 또는 폴더가 존재하면 True
# 없으면 False 반환
is_exists = os.path.exists(target_path)


print(f"파일 존재 여부: {is_exists}")


# if문으로 존재 여부에 따라 다른 메시지 출력
if is_exists:
    print(f"파일 있음: {target_path}")
else:
    print(f"파일 없음: {target_path}")


print("===============실습 5================")
# datetime을 이용해 점검 시간 기록하기


import datetime

# 현재 폴더의 파일 목록 가져오기
files = os.listdir(".")


# len()
# 리스트 안 데이터 개수 확인
file_count = len(files)


# datetime.datetime.now()
# 현재 날짜와 시간 가져오기
now_time = datetime.datetime.now()


# f-string을 이용해 문자열과 변수 함께 출력
print(f"파일 {file_count}개, 점검 시각 {now_time}")


print("===============실습 6================")
# 폴더 안에서 csv 파일만 찾아 목록 만들기


target_dir = "data"


# data 폴더가 존재하는지 확인
# 있으면 data 폴더 사용
# 없으면 현재 폴더 사용
if os.path.exists(target_dir):
    search_dir = target_dir
else:
    search_dir = "."


# 지정한 폴더 안의 전체 파일 목록 가져오기
all_files = os.listdir(search_dir)


# csv 파일만 저장할 빈 리스트 생성
csv_files = []


# 전체 파일을 하나씩 확인
for name in all_files:

    # 파일명이 .csv로 끝나는지 확인
    if name.endswith(".csv"):

        # 폴더명 + 파일명을 합쳐 전체 경로 생성
        full_path = os.path.join(search_dir, name)

        # 리스트에 추가
        csv_files.append(full_path)


# 찾은 csv 파일 목록 출력
print("[CSV] 목록:", csv_files)
