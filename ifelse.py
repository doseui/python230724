# ifelse.py

# score = int(input("점수를 입력:"))

# if 90 <= score <= 100:
#     grade = 'A'
# elif 80 <= score <90:
#     grade = 'B'
# elif 70 <= score < 80:
#     grade = 'C'
# elif 60 <= score < 70:
#     grade = 'D'
# else:
#     grade = 'F'

# print("등급은 ", grade)



print("-----break-----")
lst = range(1,11)
for i in lst:
    if i > 5:
        break
    print("Item:{0}".format(i))



print("-----continue-----")
lst = range(1,11)
for i in lst:
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))



# 반복문
value = 5
while value > 0:
    print(value)
    value -= 1

lst = ["apple", 100, 3.14]
for item in lst:
    print(item, type(item))


d = {"apple":100, "orange":200, "banana":300}
for key,val in d.items():
    print(key,val)


print("-----range함수-----")
print(list(range(10))) # 0부터 시작하여 10-1까지 (10개)
print(list(range(1,11)))
print(list(range(10,0,-1)))
print(list(range(2000,2024)))



# 파이썬 언어는 함축을 선호함
# 긴 단어도 함축
print("-----리스트컴프리헨션-----")
lst = list(range(1,11)) # 1부터 11-1까지
print([i**2 for i in lst if i > 5])

tp = ("apple", "banana", "orange")
print([len(i) for i in tp])

d = {100:"apple", 200:"kiwi"}
print([v.upper() for v in d.values()])


for i in map(lambda x:x+10, lst):
    print(i)
