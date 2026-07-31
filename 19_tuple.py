# =======================================
print("==========tuple==========")

# 기존 list의 가독성과 호환성이 불편해 tuple과 set이 생김.
# 기본 구성 : ( ,)으로 데이터를 묶고 , 으로 여러형의 자료형의 값을 저장(, 는 마지막 값에 꼭 붙여야 한다.)
# 짝 지어진 값을 하나로 묶을 때 사용 가능한 자료형

# 예시 1
sensor = ("모터 온도", 78)  # 일반
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # class <tuple>

# tuple이 판단 기준
## tuple이 되는 기준은 기본 구성 요소인 ( )와 ,의 여부이고 이 두 개의 구성 요소 중 , 만 있더라도 tuple이 만족함.
## 예외로 () 안에 아무런 값이 없다면 값을 구분 지을 필요가 없기에 tuple의 기본 구성 요소인 ()으로 tuple이 만족함.

# 요소(값)의 개수
## 요소 2개 이상 : 쉼표가 있다면 tuple
## 요소 1개 : 쉼표 여부(끝에)
## 요소 0개 : ()의 여부

# 예시로 보는 tuple의 기준
## (1) >> int
## (1,) >> tuple

# tuple의 index
sensor = ("모터 온도", 78)
print(sensor[0])

# tuple의 slice(ing)
s = (
    "a",
    "b",
    "c",
    "d",
    "e",
)
print(s[1:4])  # type : class <tuple>

# tuple unpacking : tuple에 담긴 값을 변수로 한 번에 분리

# 복습) 복수의 변수 한 번에 선언 할 떄, a,b,c = "a","b","c" 의 형태를 따른다.
# tuple에 적용 시켜 보기
unpacking = (
    1,
    2,
    3,
)  # 각각 변수 one, 변수 two, 변수 three로 선언할려고 한다.
# unpacking = one, two, three >> 이 줄의 의미는 one two three의 변수를 unpacking에 할당하는 의미 따라서,
one, two, three = unpacking  # 으로 = 기준으로 좌 우를 바꾸면 가능하다.
print("one:", one)
print("two:", two)
print("three:", three)

# 응용) list unpacking 가능할까?
one, two, three, four = [11, 22, 33, 44]
print("one:", one)
print("two:", two)
print("three:", three)
print("four:", four)


# tuple 과 list의 가장 큰 차이점은 수정 가능성이다.
## tuple은 절대 수정이 불가하다. >> 이후 원본의 변경을 막는 기능이다.
## 따라서 내림차순, 오름차순, 뒤집기 등등 원본에 영향을 주는 메서드는 사용이 불가하다.(Error 발생)

# =======================================
print("==========tuple 활용==========")

# len, .count, .index 활용이 가능하며, 원래 배운 기능과 똑같다.
# 예시 1)
tup = (
    "normal",
    "normal",
    "warning",
    "normal",
    "warning",
)
print(len(tup))  # 5 (tup의 데이터 총 길이 = 총 갯수)
print(tup.count("warning"))  # 2 (특정 데이터 갯수)
print(tup.index("warning"))  # 2 (특정 데이터가 처음 등장하는 인덱스 번호)

# =======================================
print("==========tuple의 list==========")

# list 내부의 tuple을 담은 것.
# 접근 방식
## list를 사용해서 list 내부에 접근하고, tuple에 담긴 정보를 사용 할 수 있음.(for문)
## unpacking을 사용해서 tuple에 접근한다.

# tuple의 반복문(for문)

temps_13 = [
    ("qox_001", 81),
    ("qox_002", 88),
    ("qox_003", 95),
    ("qox_004", 89),
]

warning = 90

for name, temp in temps_13:
    if temp >= warning:
        print("경고", name, "설비 온도 이상")

## list 내부의 tuple 개수가 늘어나면 for문에서 변수를 여러개 작성하면 된다. (tuple 데이터 갯수 == for문 변수 갯수)

tup_list = [
    ("일", "one", 1, "1"),
    ("이", "two", 2, "2"),
]
for kor_str, eng_str, num, num_str in tup_list:
    print("kor_str:", kor_str, "eng_str:", eng_str, "num:", num, "num_str:", num_str)

# list로 감싼 tuple은 차순이나 순서 뒤업기도 가능하다.(정렬 기준은 key라고 부른다.)
## sorted()를 이용하여, 리스트의 튜플을 특정값으로 정렬이 가능하다. >> 리스트의 정렬된 데이터를 새 변수에 반환
## 즉, 원본의 변경은 없으므로 리스트 내부의 튜플 정렬은 가능한 것이다.
# 예시 2)
temps_13 = [
    (81, "qox_001"),
    (88, "qox_002"),
    (95, "qox_003"),
    (89, "qox_004"),
]
hot = sorted(temps_13, reverse=True)
print(hot)

# =======================================
print("==========실습 1==========")

s1 = ("베어링진동", 0.8)
print(s1)  # ('베어링진동', 0.8)

print(s1[0])  # 베어링진동
print(s1[1])  # 0.8

name, value = s1
print(name, value)  # 베어링진동, 0.8

# =======================================
print("==========실습 2==========")

sensors = [("모터온도", 85), ("베어링진동", 0.4), ("펌프압력", 92), ("냉각수온도", 75)]

for name, value in sensors:
    print(name, value)

limit = 90
for name, value in sensors:
    if value > limit:
        print(name, "경고")

# =======================================
print("==========실습 3==========")

sensors = [
    ("모터온도", 85, (3, 5)),
    ("베어링진동", 0.4, (8, 2)),
    ("펌프압력", 92, (4, 8)),
    ("냉각수온도", 75, (6, 1)),
]

for name, value, pos in sensors:
    x, y = pos
    print(name, "위치:", x, y)

for name, value, pos in sensors:
    x, y = pos
    if x <= 5:
        print(name)

# =======================================
print("==========set==========")
