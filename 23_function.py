# "================================================="
print("===============함수 설계와 활용================")


# 기본값 약자
def report(name, value):
    print(f"{name}")


report("압축기A", 75.3)

# 단위마다 수치가 달라지니, 단위까지 같이 넣어주는게 데이터의 정확성이 올라간다


def report(name, value, unit="도(C)"):
    print(f"{name} : {value}{unit}")


report("압축기A", 75.3, "도(C)")
report("압축기A", 75.3)  ## unit의 언급이 하나도 없더라도 정상 출력이 가능하다.
report("압축기A", 75.3, "도(F)")

## def f(a,b,c=0) >> c의 값이 없어도 되고, 있어도 상관없다.

# 기본값 덮어쓰기


## tip: 보통 불리언의 타입을 return하는 함수는 "is_"로 시작한다.
def is_over_limit(value, limit):
    if value > limit:
        # 위험 맞음
        return True

    # 그 밖에는 위험 아님
    return False


print(f"위험한가요? {is_over_limit(95,90)}")
print(f"위험한가요? {is_over_limit(105,90)}")

## limit 값은 미리 지정해놔도 정상 출력 한다.


def is_over_limit(value, limit=90):
    if value > limit:
        # 위험 맞음
        return True

    # 그 밖에는 위험 아님
    return False


print(f"위험한가요? {is_over_limit(95)}")
print(f"위험한가요? {is_over_limit(105)}")

# 혹시라도 다른 기준을 적용해야한다면 따로 값을 기입해줘도 무방하다.
print(f"위험한가요? {is_over_limit(105, limit=80)}")

# "================================================="
print("===============지역변수와 범위================")

# scope
## 코드내의 변수 데이터의 적용 범위
