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
print(times())  # 결과 : 10(기본값) +20(기본값)
print(times(b=5))  # 결과 :  10(기본값) + 5
print(times(5))  # 결과 :  5 + 20(기본값)
print(times(5,6))  # 결과 : 5 + 6


# 키워드 인자
# default value parameter는 항상 non-default value parameter보다 뒤에 위치해야 합니다.
def connectURI(server, port="80"):
    strURL = "http://" + server + ":" + port
    return strURL

# 호출
print( connectURI("credu.com", "80"))
print( connectURI(port = "8080", server="credu.com"))



# *args (argument의 줄임말)
# non-default value parameter의 개수가 유동적일때 사용합니다.
# *args 인자 뒤에 다른 인자가 있으면 에러가 납니다.
# *args는 앞의 인자에 할당하고 남은 나머지 전부를 가져가기 때문에 
# 그 뒤의 인자가 할당받을 것이 없기 때문입니다.
def funcARGS(*args):
    return args

print( funcARGS(1,3,['1',2],{'a':1}, 1000.10) ) # 결과 : 함수 인자를 튜플로 묶어서 입력된다



# **kwargs (keyword argument의 줄임말)
# default value parameter의 개수가 유동적일때 사용합니다.
# 입력받은 인자들은 딕셔너리 형태로 저장됩니다.
# *kwargs는 *args와 마찬가지로 앞의 인자들이 할당을 받은 후 남은
# 나머지들을 모두 가져가기 때문에 맨 뒤의 순서에 위치해야 합니다.
# **kwargs는 사실상 함수의 인자 중 가장 마지막으로 오는 인자입니다.
# 따라서 뒤에 다른 인자가 붙으면 syntax error가 발생합니다.


def funcKWARGS(**kwargs):
    return kwargs

print( funcKWARGS(lang='python', number=1000, dictionary={'a':1, 'b':2}))
# 결과 : 입력 인자를 딕셔너리형태로 묶어서 입력한다.





