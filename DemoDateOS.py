# DemoDateOS.py

from datetime import*

print(dir(datetime))
print(dir())

d1 = date(2023, 7, 20)
print(d1)

d2 = date.today()   # 오늘 날짜
print(d2)
print(type(d2))

d3 = timedelta(days=100)
print(f"100일을 더하면:{d2 + d3}")
# print("100일을 더하면:{d1} {d3}".format(d2, d3))

d4 = datetime.now() # 현재 시간
print(d4)



import random
print( random.random())
print( random.random())
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print(random.sample(range(20), 10))
print(random.sample(range(20), 10))


from os.path import*

print(abspath("python.exe"))                # 전체경로
print(basename("C:/python310/python.exe"))  # 파일이름만 반환
print(getsize("c:/python310/python.exe"))

if isfile("c:/python310/python.exe"):
    print("파일 있음")
else:
    print("파일 없음")


lotto = list(range(1,46))
random.shuffle(lotto)
print(lotto)


from os import*

# print(dir())
print("운영체제이름:",name)
print("환경변수:", environ)
# print(system("notepad.exe"))

print("현재폴더:", getcwd())
chdir("..")
chdir("c:/work")

import glob
result = glob.glob("*.py") # 경로에 대응되는 모든 파일 및 디렉토리의 리스트를 반환한다
print(result)

# result = glob.iglob("*.py") # 이터레이터를 반환한다
# print(result)
# print(type(result))

for item in glob.iglob("*.*"):  # 이터레이터를 반환한다
    print(item)
