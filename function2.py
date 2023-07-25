# function2.py

# 전역변수와 지역변수
x = 1

def func(a):
    return a+x


# 호출
print(func(1))  # 결과 : 1+1

def func2(a):
    x = 5
    return a+x

# 호출
print(func2(1)) # 결과 : 지역변수 5 + 1  //  LGB(Local - Global - Builtin) 순서로 이름을 검색한다



# 기본값지정(옵션)
def times(a=10, b=20):
    return a+b

# 호출
print(times())  # 결과 : 10 +20
# print(times(,5))  # 결과 :  5 + 20
print(times(5))  # 결과 :  5 + 5
print(times(5,6))  # 결과 : 5 + 6


# 키워드 인자
def connectURI(server="multicampus.com", port):     # 
    strURL = "http://" + server + ":" + port
    return strURL

# 호출
print( connectURI("credu.com", "80"))
print( connectURI(port = "8080", server="credu.com"))
