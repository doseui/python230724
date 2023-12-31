# DemoFile.py

for i in range(0,10):
    url = "http://www.credu.com/?page=" + str(i)
    print(url)


for x in range(1,6):
    print(x, "*", x, "=", x*x)

print("-----오른쪽 정렬-----")
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).rjust(3))

print("-----0으로 채우기-----")
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).zfill(5))

print("-----서식 지정-----")
print("0x{0:X}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(150000000000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))

# 파일 쓰기
f = open("c:/work/demo.txt", "wt", encoding='utf-8')
f.write("첫번째\n두번째\n세번째\n")
f.close()

# 파일 읽기
f = open(r"c:/work/demo.txt", "rt", encoding="utf-8")
result = f.read()
# f.close()
print(result)

print("-----라인단위-----")
f.seek(0)
print( f.readline(), end="")    # str 반환 (print 함수는 출력하고 줄바꿈 한다(기본값))
print( f.readline(), end="")    # str 반환
print("-----리스트로 받기-----")
f.seek(0)
result = f.readlines()    # list 반환
print(result)

f.close()
print(result)
