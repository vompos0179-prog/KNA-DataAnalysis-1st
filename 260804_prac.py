# 260804 실습 문제


# ==============실습 2. 다중 매개변수로 센서값 계산하기================
def print_sensor_data(name, value):
    print(f"{name} {value} 도")


print_sensor_data("모터", 78)
print_sensor_data("펌프", 92)

# print_sensor_data(78, "모터")  # 78 모터 도 (의도치 않은 출력 확인)


# ==============실습 3. 키워드 인자로 함수 호출하기================
def print_sensor(name, temp):
    print(name, temp)


print_sensor(temp=78, name="모터")
print_sensor(name="펌프", temp=92)

# print_sensor("압축기", temp=85)  # 위치 인자("압축기")가 앞에 와서 정상 동작


# ==============실습 4. 반환값으로 간단 계산기 만들기================
def add_five(temp):
    return temp + 5


result = add_five(80.0)

print(result)

result_plus_five = add_five(result)
print(result_plus_five)

# ==============실습 5. 센서 통계 함수 만들기 (선택사항)================


def sensor_info(data):
    minimum = min(data)
    maximum = max(data)
    average = sum(data) / len(data)

    return minimum, maximum, average


sensor = [78, 85, 92]

minimum, maximum, average = sensor_info(sensor)

print(minimum, maximum, average)
# ==============실습 3. 처리 흐름 만들기 (선택사항)================


def average(a, b):
    return (a + b) / 2


def check(score):
    if score >= 80:
        print("평균", score, "→ 정상")
    else:
        print("평균", score, "→ 점검")


result = average(78, 92)

check(result)
# ==============실습 4. 센서 분석 함수 세트 만들기 (선택사항)================


def average(data):
    return sum(data) / len(data)


def check(avg, standard=80):
    if avg >= standard:
        return "정상"
    else:
        return "점검"


sensor = [78, 85, 92]

avg = average(sensor)
state = check(avg)

print(avg, state)
