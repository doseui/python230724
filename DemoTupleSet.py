# DemoTupleSet.py

a = {1,2,3,3}
b = {3,4,4,5}

print(a)
print(b)
print(type(a))
print(a.union(b))           # 합집합
print(a.intersection(b))    # 교집합
print(a.difference(b))      # 차집합


print("-----Tuple-----")
tp = (10,20,30)
print(tp)
print(len(tp))  # 3개
print(tp[0])    # 첫번째 성분
print("id:%s, name:%s" % ("kim", "김유신"))

# 함수 정의
def calc(a,b):
    return a+b, a*b

# 함수 호출
retValue = calc(3,4)
print(retValue)

tuA = (7,4)
print(calc(*tuA))   # 여기서 *는 튜플을 알려주는 역할 수행


print("------형식변환-----")
a = set((1,2,3))
print(a)
b = list(a)
b.append(4)
print(b)
c = tuple(b)
print(c)

