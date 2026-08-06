print("===============실습 1================")

f = open("sample.txt", "r", encoding="utf-8")

text = f.read()
print(text)

f.close()

f = open("sample.txt", "r", encoding="utf-8")

lines = f.readlines()
print(lines)

f.close()

print("===============실습 2================")

with open("memo.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요.\n")
    f.write("파일 쓰기 실습입니다.\n")

with open("memo.txt", "r", encoding="utf-8") as f:
    print(f.read())

print("===============실습 3================")

with open("memo.txt", "a", encoding="utf-8") as f:
    f.write("추가된 내용입니다.\n")

with open("memo.txt", "r", encoding="utf-8") as f:
    print(f.read())

print("===============실습 4================")

import csv

with open("data/08_press.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)

print("===============실습 5================")

import csv

with open("result.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["이름", "점수"])
    writer.writerow(["홍길동", 90])
    writer.writerow(["김철수", 85])

print("===============실습 6================")

import csv

result = []

with open("data/08_press.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    header = next(reader)

    for row in reader:
        current = float(row[4])

        if current > 90:
            result.append(row)

with open("high_current.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(header)
    writer.writerows(result)