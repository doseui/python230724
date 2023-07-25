# class1.py

# 1) 클래서 형식 정의
class Person:
    # 초기화 메서드
    def __init__(self):
        # 인스턴스 멤버변수
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))


# 2) 인스턴스 생성
p1 = Person()   # __로 시작되는 메서드는 직접 호출 못함
p2 = Person()   # 클래스 이름()는 초기화를 호출함

# 3) 메서드 호출
p1.name = "전우치"

p1.print()
p2.print()

# 런타임시에 변수 추가 (가능하지만 되도록 클래스에 추가하도록 한다)
Person.title = "new title"

# 클래스 객체와 인스턴스 객체의 이름공간이 다르다.
# 그래서 아래의 순서로 이름을 찾는다.
# 인스턴스 객체 영역 => 클래스 객체 영역 => 전역 영역
print(p1.title)
print(p2.title)
print(Person.title)

class MyClass:
    def __init__(self,value):   # 생성자 메서드
        self.value = value
        print("Instance is created! value=", value)
    def __del__(self):          # 소멸자 메서드 (알아서 해줌...)
        print("Instance is deleted!")
