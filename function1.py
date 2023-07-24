# function1.py

# 함수 정의
def setValue(newValue):
    x = newValue
    print("지역변수:", x)

# 함수 호출
result = setValue(5)
print(result)       # 반환값이 없으므로 None을 출력한다


# 함수 정의
def swap(x,y):
    return y,x

# 함수 호출
print(1,2)
print(swap(1,2))

#  교집합 문자를 리턴하는 함수
def intersect(prelist, postlist):
    # 지역변수
    result = []
    # for A in B 루프 : B에 리스트, 튜플, 문자열이 오면...
    # H(0) | A(1) | M(2)
    for x in prelist:
        # x라는 글자가 postlist에 있고 x가 result에 없으면    
        if x in postlist and x not in result:
            result.append(x)    # <-- 여기서 append를 사용하려면 리스트형 변수를 초기화해야함
    return result

# 호출
print(intersect("HAM", "SPAM"))
