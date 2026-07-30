# ======================================================
print("==========실습==========")

answer = 7
guess = 0

while guess != answer:
    guess = int(input("문제 맞춰보세요!: "))
print("정답!")

# ======================================================
print("==========실습==========")

answer = 30

while True:
    user_input = int(input("값을 입력해주세요 : "))

    if user_input > answer:
        print("Down")
    elif user_input < answer:
        print("Up")
    else:
        print("정답입니다!")
        break  # 정답을 맞혔으므로 반복문 종료

# ======================================================
print("==========실습(제미나이 버전, ppt 26)==========")

total = 0  # 5 초과 값들의 누적 합계

for i in range(1, 4):  # 총 3번 반복
    v = int(input(f"{i}번째 입력 값: "))  # 사용자가 직접 입력 (4, 7, 6)

    if v > 5:
        total += v  # 5 초과일 때만 합계에 더함
print("합계:", total)

# ======================================================
print("==========실습(강사님 코드)==========")

total2 = 0
for i in [4, 7, 6]:
    if i > 5:
        total2 += i
print("합계:", total2)

# ======================================================
print("==========실습==========")

n = int(input("횟수: "))
found = False

for i in range(n):
    v = int(input("측정값: "))

    # 기준(80) 초과를 만나면 플래그를 True 로 바꾸고 break 로 중단
    if v > 80:
        found = True
        break

# 반복 뒤 플래그로 발견 여부를 판단해 결과 출력
if found:
    print("발견")
else:
    print("없음")
