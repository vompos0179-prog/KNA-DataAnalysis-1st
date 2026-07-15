# "======================================================================="
print("===========자료형===========")
# 소수점이 없는 숫자는 정수(int) 취급(0과 음수도 정수에 포함됨.)

count = 3
age = 20
tall = 173
temp = -30
zero = 0

# 소수점이 있는 숫자는 실수(float) 취급 (5.0처럼 딱 떨어지는 수이지만 . 이 있다면 무조건 float)

tired = 99.9999
height : 17.2

# 문자열 (str) : " "로 감싼 값

hello = "안녕하세요!" 
emoji = "😊"
empty = "" # 따옴표만 있어서 문자열(str)로 취급
fake_num = "12345"
illit = "It's me" # 따옴표 종류 2가지 다 사용할 수 있는 이유

# 불린형 (bool) : 참과 거짓을 나타냄. (True,False > 대문자를 써야 bool형의 기능을 수행함.)

ok = True
no = False
# 비교 할 경우 bool로 출력
print(100<5) # False
print(5 == 5) # Ture

# type 구별 : print(type())으로 판별 가능

print(type(5)) # class int
print(type("센서")) # class str
print(type(True)) # class bool
print(type(3>2)) #class bool 
 # print 내부에 type 함수 확인 > type 내부의 연산자 확인 > 연산결과에 따른 type을 출력함.

print(3, type(3)) # 3, int

num =123
fake_num = "123"
str = "문자열"
ok = True

# 값과 type을 알기 위한 방법
print(num, type(num)) # 123 class int

# 터미널에 출력 된 자료값을 가독성을 높일 방법 (방법은 다양하니 고민해보기)
print(num, ">>>", type(num)) # 123 >>> class int
print(num, ":", type(num)) # 123 : class int

# "======================================================================="
print(3+5) # 8 class int
print("3" + "5") # 35 
print("안녕"+"하세요") # 안녕하세요 class str

# "=======================================================================
print("=====자주하는 실수=====")

# 작은 오차 해결 방법(round 함수 사용)
print(0.1+0.8) #0.9가 출력값으로 나와야 하지만 컴퓨터 내의 오차가 있어 소수점이 존재 할 수 있다.
print(round(0.1+0.8,2)) # 소수 2번째자리에서 반올림 한다.

# str과 int/float은 덧셈 불가
# print("123" + 456) # Type error 발생

print(10/2) # 5.0 > 나눗셈은 딱 나누어 떨어져도 float으로 나옴.
print(type(10/2)) # class float



# "======================================================================="
print("===========실습1===========")

