# DemoDict.py

print("-----Dict-----")
color = {"apple":"red", "banana":"yello"}   # 사전형 변수 초기화
print(len(color))
print(color)
print(color["banana"])      # 키를 가지고 값을 접근한다
color["cherry"] = "red"     # 키, 값을 새로 추가한다
print(color)

del color["cherry"]
print(color)

print(color.keys())
print(color.values())
print(color.items())

print("park" in color)     # membership test
print("moon" not in color)     # membership test

# p = phone # call by reference (파이썬은 참조형식 밖에 없음. call by value는 없음)



device = {"아이폰":5, "갤럭시":10, "윈도우":30}
print(device)

# 검색
print(device["아이폰"])
# 입력
device["맥북"] = 5
print(device)
# 수정
device["아이폰"] = 6
print(device)
# 삭제
del device["아이폰"]
print(device)

print("-----for in-----")
for item in device.items():
    print(item)

for key in device.keys():
    print(key)


# 이름 + 전화번호 맵핑(딕셔너리)
phone = {"kim":"11111", "lee":"22222", "park":"33333"}
print(phone.values())
print("kim" in phone)
print("kang" not in phone)

# 파이썬은 항상 참조를 전달한다.
p = phone
print(p)
print(id(phone), id(p))     # id는 주소는 아니지만, 주소랑 비슷한 개념의 정수를 반환

p["kang"] = "1234"

print(phone)

print("-----논리식-----")
isRight = True
print(type(isRight))
print(1<2)
print(1!=2)
print(1==2)
print( True and True and True)
print( True and True and False)
print( True or False or False)

print("-----논리식2-----")
print(bool(0))      # False
print(bool(3))      # True
print(bool(-3))     # True
print(bool("test")) # True
print(bool(None))   # False

print(bool([]))     # False
print(bool([2,3]))  # True


