# + : 더하기
# - : 빼기
# * : 곱하기
# / : 나누기

print(7 + 14)  # 21
print(7 - 14)  # -7 (계산 결과가 음수여도 출력 가능)
print(7 * 14)  # 98
print(7 / 14)  # 0.5

print(75 + 80 / 2)  # 115.0 (나누기 먼저 연산)
print((75 + 80) / 2)  # 77.5 (괄호로 감싸서 계산 순서 지정)
# =========================
print("======실습, 합/차/평균 계산======")
print("두 측정값의 합:", 7 + 77.5)
print("온도 변화량:", 77.5 - 7)
print("평균 온도:", (75 + 77.5) / 2)

temp = 25
print(temp)
score = 90
print(score)


temp = 25  # 온도 (섭씨)
count = 3  # 센서 개수
# temp = 100 # 실행안함
print(temp)  # 25

x = 5
x = 10
x = x + 1
print(x)

name = "센서 A"
temp = 30  # 온도(섭씨)
count = 10  # 센서 개수
print(name)
print(temp)
print(count)

device_temp = 30
sensor_count = 10
print(device_temp)
print(sensor_count)

x, y, z = 1, 2, 3
width, height = 4, 3
print(width)
print(height)
