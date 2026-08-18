import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv("data/students_groupby_practice.csv")


# 문제 1: 학교 전체 학생 수
student_count = len(df)

print("[문제 1] 전체 학생 수")
print(student_count, "명")


# 문제 2: 학년별 학생 수
grade_count = df.groupby("학년").size()

print("\n[문제 2] 학년별 학생 수")
print(grade_count)


# 문제 3: 학년 내 각 반별 학생 수
class_count = df.groupby(["학년", "반"]).size()

print("\n[문제 3] 학년 내 각 반별 학생 수")
print(class_count)


# 문제 4: 각 반의 국어 점수 평균
korean_mean = df.groupby(["학년", "반"])["국어"].mean().round(2)

print("\n[문제 4] 각 반의 국어 점수 평균")
print(korean_mean)


# 문제 5: 각 학년의 영어 점수 평균
english_mean = df.groupby("학년")["영어"].mean().round(2)

print("\n[문제 5] 각 학년의 영어 점수 평균")
print(english_mean)


# 문제 6: 학교 전체의 수학 점수 평균
math_mean = round(df["수학"].mean(), 2)

print("\n[문제 6] 학교 전체의 수학 점수 평균")
print(math_mean)
