# "================================================="
print("===============numpy================")

# python에서 기본 제공하는 함수 제외하고 다양한 함수를 사용하기 위해 외부에서 끌어온다.
# pypi.org 참고하면 된다.
# 하지만 pip를 터미널에서 바로 설치하면 안된다.(전체 시스템에 영향을 주기 떄문)
# 그래서 개별 Working Directory 마다 별도의 환경을 구축해 그 안의 개별 라이브러리를 따로 받아 쓴다.

# 위 설명이 바로 가상환경(venv)이다.
# 1. 현재 경로에 가상환경 설정
## python -m venv .venv

# 2. 활성화
## source .venv/Scripts/activate
## 이후, pip install numpy 입력

# 3. (작업 / 실행 끝나고,) 가상환경 종료
## deactivate

# numpy 활용 예시
import numpy as np

numbers = [1, 2, 3, 4, 5]
# 위 리스트의 값들을 이용해 numpy 배열 만들기
np_numbers = np.array(numbers)

print(np_numbers)

# numpy 활용 예시 2
import numpy as np

temp = np.array([70.5, 69.8, 73.7])

print(temp)

# 응용 : 각 항목마다 + 5를 하고 싶을때
# 기존 : for문으로 항목마다 각각 처리를 했어야 함.

print(
    temp + 5
)  # Numpy라면 간단하게 처리 할 수 있다. // 이 코드를 기존대로 해석하면 다르게 출력함.

# numpy 활용 예시 3 (arange)

import numpy as np

under_five = np.arange(5)
print(under_five)  # 0부터 n을 제외한 숫자를 출력

# 0부터 8까지 2의 간격
import numpy as np

gab_two = np.arange(0, 10, 2)
print(gab_two)


# numpy 활용 예시 4 (linspace)

# 개수 중심 균등 분할, 시작과 끝 구간을 지정한 개수만큼 나눈다.
# 0 ~ 1까지 5개로 균등 분할
import numpy as np

div_five = np.linspace(0, 1, 5)
print(div_five)

# numpy 활용 예시 5 (zeros, full)

# 0으로 채우기
block_zeros = np.zeros(5)
print(block_zeros)  # [0. 0. 0. 0. 0.]

# 7으로 채우기
block_seven = np.full(4, 7)
print(block_seven)  # [7 7 7 7]

# 명시적으로 7.0처럼 float값을 지정해줘야
# float 타입 값을로 채워지는 배열이 만들어진다.
block_seven = np.full(4, 7.0)
print(block_seven)  # [7. 7. 7. 7.]

# numpy 활용 예시 6

import numpy as np

# 0 ~ 30 6씩 증가시키면서 30보다 작은 값들을 배열 시킬떄
gab_six = np.arange(0, 30, 6)
print(gab_six)

# 0 ~ 30까지 6등분으로 나눠서 내용 채우기
div_six = np.linspace(0, 30, 6)
print(div_six)

# numpy 활용 예시 6 (측정 시간축 배열 만들기)
import numpy as np

# 특정 시간의 시작과 끝을 정하고, 간격을 정해서 배열로 만들기

checks = np.arange(0, 60, 5)
print(checks)

# numpy 활용 예시 6 (n차원)

## 기존에는 print(list[a][b])의 형식이라면 numpy에서는 print(list[a,b])으로 쓴다.
# print(list.ndim) 으로 코드를 짜면 몇 차원의 데이터 값인지 알려준다.

# .shape 로 출력하면 (a,b) a는 행 b는 열을 의미한다.
# .size 로 출력하면 a*b 값으로 출력된다.
## 열과 행의 모습은 바꿀수 있어도 데이터 총 량은 바뀌지 않는다.

# numpy 활용 예시 7 (자료형과 변환)

# .dtype 으로 출력하면 해당 데이터가 어떤 type인지 알려준다.
# .astype 은 자료형 바꾸기의 기능을 가지는데, float을 int로 바꾸면 반올림의 개념이 아니라 버림으로 변환한다.

# .reshape 배열의 모양을 바꾸는 코드, 값의 개수가 같아야 정상 출력이 가능하다.
# .reshape(a,b) a,b 중 한쪽에 -1을 넣으면 나머지 값에는 자동계산을 해준다.

# .flatten 1차원으로 데이터를 나열해준다.
