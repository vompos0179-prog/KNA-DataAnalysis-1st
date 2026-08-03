# =======================================
print("==========dictionary==========")

# 순서 번호 대신, 데이터의 이름값으로 접근하는 자료형
# key : value 구조로 되어있다.
# 리스트의 불편함으로 인해, key:value 구조로 데이터를 저장하고, key값으로 value에 접근하는 자료형이다.
# 이름으로 대상(데이터)를 찾는 것이 가능하다. (keyword으로 value에 접근)
# {key : value, key : value, key : value, ...}
# : 의 유무가 중요하다. (dictionary의 특징, 빈 {}는 dictionary를 의미한다.)

# 예시 1)
data_class_list = {
    "반장": "태구",
    "부반장": "수진",
    "당번": "영준",
}  # 같은 key값은 존재할 수 없다. (중복 불가)

# 예시 2)
sensors = {"센서이름": "보일러", "모터온도": 78, "진동": 0.4}
print(sensors)  # {'센서이름': '보일러', '모터온도': 78, '진동': 0.4}
print(type(sensors))  # <class 'dict'>
empty = {}  # 빈 dictionary
print(type(empty))  # <class 'dict'>

print(
    sensors["센서이름"]
)  # 보일러 // [ ] 안에 " "까지 입력해야 정상적인 출력이 가능하다.
print(sensors["모터온도"])  # 78
print(sensors["진동"])  # 0.4

# dictionary의 value 변경
sensors["센서이름"] = "펌프"  # dictionary의 value 변경

# dictionary의 value 추가
sensors["펌프 압력"] = 95
sensors["유량"] = 42
del sensors["유량"]  # dictionary의 value 삭제

print(sensors)

# dictionary의 없는 데이터 호출 및 확인 (get, in)

# print(sensors["유량"])  # KeyError: '유량' // 없는 key값을 호출하면 KeyError 발생
## Error 발생을 방지하기 위해, dictionary의 get() 함수를 사용하면 된다.
print(
    sensors.get("유량")
)  # None // 없는 key값을 호출하면 None, 있는 값이면 해당 value값을 출력한다.

# get 대신 in으로 해당 데이터가 있는지, 확인할 수 도 있다.
if "유량" in sensors:
    print(sensors["유량"])
else:
    print("데이터가 없습니다.")

# =======================================
print("==========keys,values==========")

print(sensors.keys())  # dict_keys(['센서이름', '모터온도', '진동', '펌프 압력'])
print(len(sensors))  # 4 // len() 함수로 key의 길이 확인 가능

print(sensors.values())  # dict_values(['펌프', 78, 0.4, 95])
print(len(sensors.values()))  # 4 // len() 함수로 value의 길이 확인 가능

# =======================================
print("==========items==========")

# for key, value in dictionary.items() : dictionary의 key와 value를 동시에 출력할 수 있다.
## key와 value를 동시에 처리.
## key와 value를 tuple형태로 묶어서 처리한다.
## 반복마다 key와 value를 자동으로 분리함.

# for key, value in sensors:
#     print(key, value)  # TypeError: cannot unpack non-iterable str object // dictionary는 key값만 반복처리 가능하다.
for key, value in sensors.items(): # key = name, value = data 와 같이 좀 더 직관적인 이름으로 설정한다.
    print(key, value)
    
