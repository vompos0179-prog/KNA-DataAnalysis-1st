# "========================================================="
print("============실습 1=============")

str = "ready"
str_update = str.upper()
print(str_update)

# "========================================================="
print("============실습 2=============")

str = "WARNING"
str_update = str.lower()
print(str_update)

# "========================================================="
print("============실습 3=============")

name = "nam jeong gon"
print(name.title())
print(name.capitalize())

# "========================================================="
print("============실습 4============")

print("ABC".isupper())
print("abc".islower())
print("Abc".islower())

# "========================================================="
print("============실습 5============")

str = "Sensor_LOG.CSV"
low = str.lower()

print(low.startswith("sensor"))
print(low.endswith(".csv"))

# "========================================================="
print("============실습 6============")

text = "python"

# 앞의 'py' + 대문자 'T' + 뒤의 'hon'
result = text[:2] + text[2].upper() + text[3:]
print(result)  # pyThon

# 소문자 t 를 대문자 T로 치환하는 방법
text = text.replace("t","T") 
print(text)

# "========================================================="
print("============실습 7============")

str = "  가동중   "
str_strip = str.strip()
print("[" + str_strip + "]") 


# "========================================================="
print("============실습 8============")

text = "     Warning     " # > [     warning    ], [warning]

print("[" + text.lower() + "]")
print("[" + text.lower().strip() + "]")