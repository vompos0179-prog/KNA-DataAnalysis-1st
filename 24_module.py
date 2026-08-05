# "================================================="
print("===============import================")

# module, package, library 의 구분
## module < package < library

# 수학 관련 모듈을 불러오기
# 예시 1)
import math

## 해당 모듈이름.함수() 의 구조로 호출한다.
result = math.sqrt(16)

print(result)

# from import  기능 일부만 가져오기
# 예시 2
## 수학 관련 모듈에서 sqrt 기능만 불러온다.
from math import sqrt

result = sqrt(16)
print(result)

### 예시 1,2번 차이는 result 부분이고, 결과값은 같다. (코드가 2번이 좀 더 간결하고, 1번은 출처가 명확하다.)

# as 별칭과 import*
# as는 numpy, pandas, matplotlib.pyplot 뒤에 붙어서 np, pd, plt 으로 줄임말로 바꿀 수 있다.
# 긴 모듈명에 as 를 붙이고 원하는 별칭으로 모듈을 끌어올 수 있다.

## 예시 3
import math as mt

result = mt.sqrt(16)
print(result)

## 예시 4
# datetime 모듈을 가져옵니다
import datetime as dt

# datetime의 now()는 현재의 지역 날짜와 시간을 반환합니다.
now = dt.datetime.now()
print(now)  # 2026-08-05 11:19:45.776780
print(type(now))  # <class 'datetime.datetime'>

# "================================================="
print("===============module================")

# math 표준 라이브러리 (예시 1)
import math

print(math.sqrt(9))
print(math.ceil(4.2))
print(2**3)

# sqrt와 ceil 두개를 써야할 때 이어서 쓰면 된다. (예시 2)
from math import sqrt, ceil

print(sqrt(9))
print(ceil(4.2))

# 표준 라이브러리의 random 모듈 (예시 3)
import random

print(random.randint(1, 10))  # .randint(a,b) a~b까지의 정수 임의값 출력
print(
    random.choice(["정상", "경고", "위험"])
)  # .choice(a,b,c, ,n) a~n까지의 임의값 출력

# 표준 라이브러리의 datetime 모듈 (예시 4)
import datetime

now = datetime.datetime.now()  # datetime 모듈의 datetime 클래스의 now( ) 함수 호출
print(now)

# 모듈 도움말 보기 (구글링해서 검색하는게 더 좋다. 하지만 인터넷이 안되는 상태라면 진행해야함.)
# dir(math) >> 해당 모듈의 함수를 목록화 해서 보여준다.
# help(math.sqrt) >> 해당 모듈의 함수의 기능을 설명한다.

# "================================================="
print("===============경로================")

# 절대경로 와 상대경로
# 예를 들어 24_module.py를 바탕화면에서 열어야한다고 가정하면
# 절대 경로의 예시 : C:\Users\desktop\바탕화면\python\24_module.py
# 상대 경로의 예시 : code .\Desktop\24_module.py 를 빈 터미널에 입력하면 창이 열린다.

# 표준 라이브러리의 os 모듈 >> 현재 작업 디렉토리의 절대 경로 반환 (예시 5)
import os

current_working_dir = os.getcwd()
print(current_working_dir)

# 표준 라이브러리의 listdir 모듈 >> 현재 작업 디렉토리의 파일 목록 가져오기 (예시 6)
file_list = os.listdir()
for file_name in file_list:
    print(file_name)

# 표준 라이브러리의 os 모듈의 응용 >> 해당 파일의 존재를 확인 (예시 7)
# os.path.join( ) >> 경로를 반환해줌
# os.path.exists( ) >> True , False 로 반환해줌
path = os.path.join("data", "08_press.csv")
print(path)

if os.path.exists(path):
    print(f"파일 있음: {path}")
