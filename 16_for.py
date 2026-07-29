# =======================================
print("==========range==========")

# 반복문은 동일한 작업을 특전횟수만큼 반복해야할 때, 코드를 길게 쓰지 않고도 반복시킬수 있음.
# 기본 구조 >> for 변수 in range(횟수):
## 반복 시킬 코드(들여쓰기 한 칸 필수), 복사 붙여넣기로 여러번 쓰는 대신 'n번 실행해라' 라는 의미.

## range 응용 > range(a,b,c) >> a부터 b까지 c칸마다 건너뛰기 후 출력.

print("=====for문 예시=====")
for i in range(3):
    print("안녕하세요!")  # 들여쓰기는 필수! , i 라는 변수를 굳이 쓰지 않아도 된다.

# 0 ~ 10까지의 숫자 자체가 필요하거나 출력 할 떄
for i in range(11):
    print(i)  # i는 증가값을 지정하지 않는 이상 반복할 때 마다 자동으로 +1이 적용됨.

# 짝수 출력
for i in range(0, 11, 2):
    print(i)  # range(a,b,c) >> a부터 b까지 c칸마다 건너뛰기 후 출력.

# 홀수 출력
for i in range(1, 10, 2):
    print(i)

# 역순 출력
for i in range(10, 0, -1):
    print(i)

# 역순 + 짝수 출력
for i in range(10, 0, -2):
    print(i)


# # 누적 변수(나중에 강사님 코드 보고 보충 하기)
# total = 0

# for i in range(1, 6):


# for문 안에 누적변수 선언 시
# for i in range(1, 6):
#     total2 = 0  # 반복을 돌 때 마다 새로이 변수에 값이 0으로 할당
#     print("total2 = 0 시 total2에 할 당 된 값:", total2)
#     print(
#         "현재 i 값 :", i)
#     tatal2 += i
#     print("total2 += i 후의 total2에 할당된 값: ", total2)
# print("합계: ", total2)

# 번외
if 3 == 3:
    hi = "안녕"
print(hi)  # python에서는 if문 안의 변수도 어디서든 호출 가능한 변수로 선언됨.

# 1~15 사이의 4의 배수만 누적
total3 = 0
for i in range(1, 16):
    if i % 4 == 0:
        total3 += 3
print("1~15 사이의 4배수 누적 결과: ", total3)

# =======================================
print("==========enumerate==========")

# eumerate : 사전적 의미는 '낱낱이 세다'
temps = [33, 23, 45, 32, 28]

for t in enumerate(temps):
    print(
        t
    )  # (인덱스 숫자, 인덱스 별 값) >> 범위를 지정하지 않아도 리스트의 모든 요소를 순환.
    # 출력 형식이 알아보기 힘들다. 라는 단점을 가지고 있다.
    # eumerate를 사용 할 때, 변수는 2개를 전달한다. (하단 과 같은 결과가 나온다.)

for idx, t in enumerate(temps):
    print(f"idx: {idx}, t: {t}")

# ==========예시==========
# 안녕의 인덱스 출력하기 위해서는 해당 값과 인덱스 번호 둘 다 필요하다.

list = ["안녕", "hi", "hi", "안녕", "hi", "안녕"]
for idx, value in enumerate(
    list
):  # idx로 인덱스 번호를, value로 인덱스의 해당 값을 분리해준다.
    # 이를 도와주는 내장함수가 enumerate이다.
    # enmuerate는 애초에 값을 두 개 반환을 해주는데 (인덱스 번호, 인덱스 번호의 값)
    # 이기 떄문에 변수를 따로 따로 지정을 해주면 그 값들을 분리해준다.
    # 하지만 굳이 굳이 enumerate를 쓰지 않아도 된다.(하단 코드 참고)

    for i in range(len(list)):
        print(
            list[i]
        )  # 바로 위 enumerate를 쓰는 내장함수와 출력값은 똑같다. 방법은 많으니 너무 한가지에 집중 X

# =======================================
print("==========반복문 예시(구구단)==========")

# ===========STEP 1(단 하나만 출력)==========
# 3단
for i in range(1, 10):
    print("3 X ", i, "=", 3 * i)

# ===========STEP 2(여러단 동시에 출력)==========
for dan in range(2, 10):  # 바깥 : 2단, 3단 *** 9단
    for su in range(1, 10):  # 안쪽 : 1 ~ 9
        print(dan, "x", su, "=", dan * su)
    print("=====")

# =======================================
print("==========반복문 예시(피라미드)==========")
