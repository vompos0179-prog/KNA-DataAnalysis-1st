# "================================================="
print("==============매개변수=================")

# 간단한 인사말을 함수로 만든다고 가정하면, 사람마다 인사말을 만들어야 하기때문에
# 코드의 반복이나, 함수가 길어질 수 밖에 없다.
# 해결책은 하나의 함수에서 다양성을 제공할 수 있어야하고, 이것이 매개변수이다.


# 예제 1)
def say_hi(name):
    print(f"안녕하세요, {name}")


say_hi("Ned")
say_hi("Tuna")
## name이 이때 매개변수로 작용을 한다.


# 예제 2)
def check(name):
    print(f"{name} 장비의 점검을 시작합니다.")


check("압축기A")
check("펌프B")


# 예제 3) 매개 변수가 2개 이상인 함수
# STEP 1
def calc_sum():
    number_a = 1
    number_b = 2
    total = number_a + number_b
    print(f"{number_a}+{number_b}={total}")


calc_sum()

# ================================================
# STEP 2


def calc_sum(number_a, number_b):
    # number_a = 1
    # number_b = 2
    total = number_a + number_b
    print(f"{number_a}+{number_b}={total}")


calc_sum(1, 2)


# 장비 이름과 온도 정보 출력
def report(name, temp):
    # name = "압축기A"
    # temp = "75.3"
    print(f"{name}의 온도는 {temp} 도 입니다.")


report("압축기A", 75.3)
report("펌프B", 85.2)

## name 과 temp를 반대로 기입하지 않도록 주의!!
## 변수의 갯수가 맞지 않을때는 TypeError 발생함.

# 키워드 인자 없이 함수 호출
# report_keywords("펌프A", 37.4)
# report_keywords(37.4, "펌프A")
## 펌프 앞에 name, 각 온도 앞에 temp를 쓰면 휴먼 에러를 줄일 수 있다.

# "================================================="
print("==============반환값(return)=================")


def add(a, b):
    return a + b


print(add(1, 2))
print(add(2143, 3143))
print(add(342, 111))

# 예제) 여러번 같은 결과 호출해야한다면 변수에 담아 쓰기
result = add(1, 2)
print(result + 1)
print(result + 2)
print(result + 3)


# 예제) 평균 내는 함수 만들기
def calc_average(a, b):
    return (a + b) / 2


avg = calc_average(75.3, 88.0)
print(f"평균 온도: {avg}")


# 예제) 여러 값을 한번에 반환하기
## value의 배열을 받고, min과 max을 동시에 return 하기
def calc_min_max(values):
    mininum = min(values)
    maxinum = max(values)
    # i) print(mininum, maxinum)
    return mininum, maxinum  # 두번쨰 방법


target_list = [1, 2, 3, 4, 5, 6]
result = calc_min_max(target_list)
print(result)  # tuple을 확인

# 반환값을 언패킹으로 받기 >> 개별 변수에 담아두고 이후 활용하기
result_min, result_max = calc_min_max(target_list)
print("최솟값", str(result_min))
print("최댓값", str(result_max))

# 예제) return으로 반환 받은 값은 none이 된다.


def say_greet():
    print("만나서 반갑습니다.")
    return


greet = say_greet()
print(greet)  # None
