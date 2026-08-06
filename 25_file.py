# "================================================="
print("===============open================")

# open(파일명,모드,인코딩) >> 내장함수
f = open("sample.txt", "r", encoding="utf-8")  # r = 읽기모드, utf-8 형식
# 읽기모드(r)로 utf-8 형식의 변환을 거쳐 가져온 파일의 참조값을 f 변수에 담는다.

print(type(f), __name__)

# 텍스트 파일 한줄씩 문자열 만들기
lines = f.readlines()
print(lines)

f.close()  # open으로 열었다면, .close 메서드를 사용해 닫아준다.

## encoding : 글자가 깨지거나 할 수 있기 때문에 utf-8 이외에 cp949 등 다양한 코드를 알고있어야 한다.
## 모드 : r(읽기), w(새로 쓰기), a(이어 쓰기)
## 내부 데이터에 따라서 .read, .readline, .readlines 를 쓴다.

# "================================================="
print("===============with open================")

# with open (...) as f 의 형태를 따르며, ...에 "파일명", "r", encoding="utf-8"이 들어간다.
# with를 쓰게 되면 .close를 따로 쓰지 않아도 된다.

# 모드 r 대신 w를 쓰게 되면 기존 파일은 덮어쓰기, 없는 파일이면 생성 후 쓰기(새로쓰기)로 적용된다.
# with open ("sample.txt", "w", encoding="utf-8") >> sample.txt 파일을 만들거나, 덮어쓰기를 진행한다.

# 모드 a를 쓰게되면 이어 쓰기가 되며, 파일이 있어야 진행이 된다.(기존 내용이 보존됨.)
# with open ("sample.txt", "a", encoding="utf-8") >> sample.txt 파일의 기존 내용 뒤에 이어쓰기가 진행된다.

# "================================================="
print("===============csv 파일================")

# csv 파일 일련의 접근 방향

import os
import sys
import csv

csv_path = os.path.join(
    "data", "08_press.csv"
)  # join이므로 해당 파일의 경로를 출력해준다.

if os.path.exists(csv_path):
    print("파일을 찾았습니다.")
else:
    print("파일이 없습니다. 프로그램을 종료합니다.")
    sys.exit(1)

print("===============================")

with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    for row in reader:
        print(
            row
        )  # row 라는게 행이라는 의미로 출력값이 각 행별로 정리된 모양으로 나온다.
        print(
            row[0]
        )  # 출력값의 타입이 리스트의 형식이기 때문에 [0]으로 넣으면 인덱스 0번만 출력이 된다.

## 위의 코드를 정리하면 “08_press.csv를 읽기 모드(UTF-8)로 열고,
# csv.reader()로 CSV 파일을 한 행씩 리스트 형태로 읽어, 반복문에서 각 행(row)을 출력한다.” 라는 의미이다.

# "================================================="
print("===============csv 파일2================")

import os
import sys
import csv

csv_path = os.path.join("data", "result.csv")

with open(csv_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["시각", "설비"])
    writer.writerow(["09:00", "PUMP-01"])
    writer.writerow(["10:00", "PUMP-02"])
