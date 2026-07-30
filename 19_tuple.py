# =======================================
print("==========tuple,set==========")

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
