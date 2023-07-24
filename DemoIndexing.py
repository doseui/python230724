# DemoIndexing.py
strA = "python is very powerful"
print(strA[0])
print(strA[1])
print(strA[0:3])

# 축약된(약식) 표현식
print(strA[:3])


# 디버깅하지 않고 바로 실행 : ctrl + f5
print(strA[-3:]) # 뒤에 3 문자
print(strA[-8:]) # 뒤에 8 문자

# 리스트 연습
color = ["red", "blue", "green"]
print(color)
print(len(color))
print(type(color))
print(color[0])

# 디버깅할 때 중단 wja(breakpoint)
for item in color:
    print(item)

color.append("white")
print(color)

color.insert(1, "pink")
print(color)

print(color.insed("red"))
color += "red"
print(color.pop)
print(color.pop(1))
print(color)

color.extend("bloack", "red", "white")


print(color)




