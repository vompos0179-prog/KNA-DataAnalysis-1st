# 조건문 - if
# 항상 실행되지 않고 조건에 따라서
# 실행되는 코드가 달랐으면 할 때 사용
# 코드의 분기라고도 표현
# 조건문의 조건은 True와 False로 결과가 나와야 함

# if 조건식:
#   실행할 코드 (한 칸 들여쓰기)

# if문의 :은 그 다음 올 코드가
# if문 조건식 결과가 True일 때만 실행하라는 의미
# 즉, 여기서부터 이 조건에 속한다 라는 신호
# 조건의 속하는 코드는 모두 들여쓰기가 적용되어 있어야 함


temp = 85

if temp > 80:  # 만약에 temp라는 변수의 담긴 값이 80보다 크다면?
    print("temp 변수의 값이 80보다 크다!!!")  # 들여쓰기 된 코드 실행
    print("🚨")
print("이건 항상 실행되는 코드")

temp = 50
if temp > 80:  # 50이 80보다 큰 지 비교하고 False라는 결과를 확인하면
    # 들여쓰기 된 코드는 실행 안함
    print("temp 변수의 값이 80보다 크다!!!")
    print("🚨")
print("이건 항상 실행되는 코드")  # 이 코드만 실행

# temp 변수의 값이 80보다 크다면 "경고" 출력
# temp 변수의 값이 80 이하라면 "정상" 출력
# 위 두 가지를 모두 하고싶은 경우

temp = 70  # 1, 2안 모두 정상 동작
temp = 90

# 1안
if temp > 80:
    print("경고")
print("정상")  # if문 밖의 코드는 무조건 실행됨
# 이 경우에는 temp 변수의 값이 90이어도 실행되는 것

# 2안 > else 사용
if temp > 80:  # if문의 조건이 True일 때만 출력
    print("경고")
else:  # if문의 조건이 False일 때만 출력
    print("정상")  # 항상 실행되지 않음
# if문의 코드블럭과 else문의 코드블럭은 절대 동시에 실행되지 않음
# 둘 중의 하나만 실행
# 1개의 분기로 코드를 실행해야할 때 사용

# if문 실습
# 사용자에게 나이를 입력받아 성인인지 출력하는 조건문 작성하기

print("=== 실습 1 ===")

age = int(input("나이를 입력하세요: "))
if age >= 19:
    print("성인입니다")
else:
    print("미성년자입니다")

# if문 실습2
# 숫자 맞추기 게임
# 정답을 맞추면 맞았습니다, 틀리면 틀렸습니다 출력


# 예시)
# 정답을 50으로 지정
# 사용자에게 입력값을 받기
# 사용자 입력값이 정답과 동일하다면 "정답입니다" 출력
# 사용자 입력값이 틀렸다면 "틀렸습니다" 출력
# 마지막으로 무조건 "게임이 종료되었습니다"
answer = 50
user_answer = int(input("숫자를 맞춰주세요: "))
if answer == user_answer:
    print("정답입니다😻")
else:
    print("틀렸습니다😿")
print("게임이 종료되었습니다💕")

# 신호등 색을 입력받아서
# "초록색"이라면 "건너세요" 출력
# "빨간색"이라면 "기다리세요" 출력
# 입력값이 초록색이나 빨간색이어야만 정상 동작
# 이상한 값 입력 시 "다시 입력하세요" 출력

user_input = input("신호등 색을 입력하세요 (빨간색, 초록색만 입력 가능): ")

# or 사용 + if문 중첩
if user_input == "초록색" or user_input == "빨간색":
    # user_input이 "초록색" 이거나 "빨간색"일 때만 실행
    if user_input == "초록색":
        print("건너세요")  # 중첩 if문은 들여쓰기 더 주의
    # if user_input == "빨간색": # else문과 동일하게 동작
    #     print("기다리세요")    # 하지만 else를 사용하는게 효율적
    else:
        print("기다리세요")
    # 사용자 입력값이 "초록색" 이거나 "빨간색"일 때 무조건 출력
    print("이건 언제 실행될까?")
else:
    print("다시 입력하세요")


if user_input == "초록색":
    print("건너세요")
if user_input == "빨간색":
    print("기다리세요")
else:
    print("다시 입력하세요")

# =========================
# and 연산자 + if문 중첩

# 정상 체온 범위 : 36.2~36.9
user_a = float(input("체온을 입력해 주세요: "))
if user_a >= 36.2 and user_a <= 36.9:
    print("당신은 정상체온입니다.")
else:
    if user_a > 36.9:
        print("당신은 열이 나고 있습니다.")
    else:
        print("당신은 저체온입니다.")
print("체온 판단 완료")

# elif
# 위의 체온 판단 if문 안에서 열나는지 저체온인지 판단하도록 수정
# if문 중첩 자체는 무한히 가능
# 권장하는 방법은 아님

if user_a <= 36.2:
    print("당신은 저체온 입니다.")
elif user_a >= 36.9 and user_a < 37.8:
    print("당신은 미열입니다. 주의하세요")
elif user_a >= 37.8:
    print("당신은 고온입니다. 병원에 방문하세요.")
else:
    print("당신은 정상 체온입니다.")
print("체온 확인 완료")

# elif의 순서
# 
score = 100


# 100이기 때문에 우수가 출력되어야 하지만
# 코드의 순서가 적합하지 않아서 "미흡"이 출력됨
if score >= 50:
    print("미흡")
elif score >= 90:
    print("우수")
elif score >= 70:
    print("보통")
else:
    print("비상")

# 정상 출력
if score >= 70:
    print("보통")
elif score >= 90:
    print("우수")
elif score >= 50:
    print("미흡")
else:
    print("비상")

# not 연산자
# 괄호로 감싸서 사용
if not(3 == 5):
    print("출력됩니다")
# 3과 5는 같지 않으니 False가 되지만 
# 앞에 not이 있어서 False를 True로 뒤집어 if가 인식

# if문은 줄바꿈을 하지 않아도 :을 기준으로 동작 자체는 가능
# 하지만 줄바꿈해서 가독성을 높이길 권장
# 탭은 아직 위의 코드가 끝나지 않았고 한 줄이라는 것을 명시


# score = 82
# if score >= 90: print("우수")
#elif score >= 70: print("미흡")
# elif: print("미흡")

print("=== 실습 2 ===")

temp = int(input("측정 온도를 입력 하세요"))
if temp > 80:
    print("위험")
elif temp > 60:
    print("주의")
else:
    print("정상")

# ===== 실습 3

correct_id = "admin"
correct_pw = 1234
user_id = input("아이디: ")
user_pw = input("비밀번호")
if user_id ==correct_id and user_pw == correct_pw:
    print("로그인 성공")
else:
    print("로그인 실패")

# =============실습5
temp = int(input("온도: "))
vib = float(input("진동: "))
current = int(input("전류: "))
if temp > 80 or vib > 4.0:
    print("위험: 즉시 정지")
else:
    if current > 60 and temp > 70:
        print("주의: 부하 점검")
    elif vib > 2.5:
        print("주의: 진동 관찰")
    else:
        print("정상")


