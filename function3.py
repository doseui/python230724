# function3.py

# 가변인자
def union(*ar):
    # 지역변수 리스트
    result = []
    for item in ar:     # 단어 단위로 나누기
        for x in item:  # 문자 단위로 나누기
            if x not in result:
                result.append(x)
    return result


# 호출
print( union("HAM", "SPAM"))
print( union("HAM", "SPAM", "EGG"))






# 람다함수
g = lambda x,y:x*y  # globals에 남아 있음

print( g(3,2) )
print( g(5,6) )
print( (lambda x:x*x)(3) ) # 함수를 정의하고 인자를 전달. globals에 남아 있지 않음
print( globals() )



# 내장함수 필터
# 필터링 함수 정의
# def getBiggerThan20(i):
#     return i>20

lst = [10, 25, 30]
# iterL = filter(getBiggerThan20, lst)
# for i in iterL:
#     print(i)

print("-----람다함수-----")
iterL = filter(lambda x:x>20, lst)  # 함수 인자로 None이 넘어가는 경우, 람다로 정의하는 경우가 많다
for i in iterL:
    print(i)



