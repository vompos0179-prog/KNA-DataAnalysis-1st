# =======================================
print("==========여러 값이 포함된 list==========")

# 조건문을 통해 리스트들의 값들을 검사?하는 과정 >> 만족, 불만족하는 값들에 대해 반복을 멈추거나 계속 진행함.

# ======(실습)======
temps = [25, 32, 28, 35, 19, 31, 27]

for t in temps:  # for로 값을 하나씩 꺼내며 if로 30 이상인지 검사
    if t >= 30:  #  조건에 맞는 값만 안내 문구와 함께 출력
        print("고온:", t)

# ======(실습)======

# ① 임의의 가동 시간(숫자) 리스트 지정
hours = [2, 5, 7, 11, 6, 10, 15, 1, 9]

# ② for로 값을 하나씩 꺼내며 5 이상이면서 10 이하인지 and로 검사
for h in hours:
    if h >= 5 and h <= 10:
        # ③ 두 조건을 모두 만족하는 값만 출력
        print("조건 만족 가동 시간:", h)

# ======(실습)======

# 임의의 온도 리스트 저장 및 합계/개수 변수 준비
temps = [22, 34, 18, 31, 29, 35, 26, 32]
total = 0
count = 0

# for 안에서 if로 30 초과 검사
for t in temps:
    if t > 30:
        # 조건에 맞는 값만 합계에 더하고 개수 1 증가
        total += t
        count += 1

# 고온 평균 구하기 (30 초과인 값이 1개 이상일 때만 계산)
if count > 0:
    average = total / count
    print("고온 평균:", average)
else:
    print("30도를 초과하는 값이 없습니다.")

print("==========list 필터링==========")

# 예시 1
temps = [1, 5, 2, 7, 4, 8, 10, 3]
high = []
low = []

for t in temps:
    if t < 5:
        low.append(t)
    else:
        high.append(t)

print("high :", high)
print("low :", low)

## 추가 >> 오름, 내림차순으로 정리해보기
# for문의 과정에서 나오는 값의 분류는 따로 반환을 하지않기 떄문에 차순으로 정리할려면 따로 변수에 저장해야한다.


# 작업 순서
# 출력(for로 print) >> 조건 추가(for + if/else 등)로 선별 >> 연산/계산 >> 빈 리스트에 추가

# ======(실습)======

# 임의의 온도 리스트 저장 및 빈 리스트 준비
temps = [24, 33, 29, 36, 27, 31, 22, 35]
hot = []

# for/if 구절로 30 초과인 값만 append로 새 리스트에 담기
for t in temps:
    if t > 30:
        hot.append(t)

# 완성된 새 리스트와 개수(len) 출력
print("30도 초과 온도 리스트:", hot)
print("고온 개수:", len(hot))

# ======(실습)======

# ① 임의의 섭씨온도 리스트 저장 및 빈 리스트 준비
temps_2 = [20, 25, 15, 30, 28]
temps_3 = []

# ② for 문으로 각 값을 화씨(섭씨 * 1.8 + 32)로 계산하여 append
for c in temps_2:
    f = round(c * 1.8 + 32, 2)
    temps_3.append(f)

# ③ 완성된 화씨 리스트 출력
print("화씨온도 리스트:", temps_3)


print("==========list 속의 list==========")

# 예시 1
rows = [["펌프", 25], ["모터", 32], ["압축기", 28]]
## 표(행과 열의 형식)처럼 한 줄에 여러 데이터가 묶인 데이터, 가장 큰 대괄호를 행 / 내부의 대괄호를 열 로 취급한다.

print(rows[0])  # ["펌프", 0]
print(type(rows[0]))  # <class 'list'>

## 대괄호 속 내부의 대괄호 데이터 접근
print(
    rows[1][1]
)  # 32 >> [1[1]]이 아닌 [1][1]와 같이 이어서 코드를 써야 안에 있는 데이터로 접근이 가능하다.

# list 내부 list의 온도 값만 출력
for row in rows:
    print(row[0], "온도", row[1])  # 펌프 온도 25
## rows는 가장 바깥의 대괄호이고, row는 내부의 리스트들을 뜻한다. 따라서 row[1]이 25가 되는것이다.

# ======(실습)======

temps = [25, 32, 28, 35, 27, 31, 24, 33, 29, 36]
total = 0

# 전체 평균 구하기
for t in temps:
    total += t
print("전체 평균:", total / len(temps))

# 고온 데이터(30 초과)만 골라 새 리스트 만들기
hot = []
for t in temps:
    if t > 30:
        hot.append(t)

# 고온 개수 및 고온 평균 구하기
hot_total = 0
for h in hot:
    hot_total += h

print("고온 개수:", len(hot))
print("고온 평균:", hot_total / len(hot))
