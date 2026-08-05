print("===============실습 1================")

import math
from math import sqrt

res1 = math.sqrt(16)
res2 = sqrt(16)

import math as m

res3 = m.sqrt(16)

print(res1)
print(res2)
print(res3)

print("===============실습 2================")

import random

sensor_value = random.randint(1, 100)
print(f"생성된 센서값: {sensor_value}")

processed_value = math.sqrt(sensor_value)
print(f"센서의 제곱근): {processed_value}")

print("===============실습 3================")

import os

current_path = os.getcwd()
print(f"현재 작업 경로: {current_path}")

file_list = os.listdir(".")

print("\n--- 전체 파일 목록 ---")
for name in file_list:
    print(name)

print("\n--- CSV 파일만 출력 ---")
for name in file_list:
    if name.endswith(".csv"):
        print(name)

print("===============실습 4================")

target_path = os.path.join("data", "08_press.csv")

is_exists = os.path.exists(target_path)
print(f"파일 존재 여부: {is_exists}")

if is_exists:
    print(f"파일 있음: {target_path}")
else:
    print(f"파일 없음: {target_path}")

print("===============실습 5================")

import datetime

files = os.listdir(".")
file_count = len(files)

now_time = datetime.datetime.now()

print(f"파일 {file_count}개, 점검 시각 {now_time}")

print("===============실습 6================")

target_dir = "data"

if os.path.exists(target_dir):
    search_dir = target_dir
else:
    search_dir = "."

all_files = os.listdir(search_dir)

csv_files = []

for name in all_files:
    if name.endswith(".csv"):
        full_path = os.path.join(search_dir, name)
        csv_files.append(full_path)

print("[CSV] 목록:", csv_files)
