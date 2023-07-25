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



print("-----range함수-----")
print(list(range(10)))
print(list(range(1,11)))
print(list(range(10,0,-1)))
print(list(range(2000,2024)))




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


