class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name,
             self.phoneNumber)) 
    def working(self):
        print("현재 작업중")
    def coding(self):
        print("현재 코딩중")


class Student(Person):  # Person을 상속한다
    # 상속받고 덥어쓰기(재정의, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        Person.__init__(self, name, phoneNumber)
        # self.name = name
        # self.phoneNumber = phoneNumber
        self.subject = subject
        self.studentID = studentID
    # def printInfo(self):
    #     return super().printInfo()
    # 재정의
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name,
             self.phoneNumber))
        print("Info(subject:{0}, studentID: {1})".format(self.subject,
             self.studentID))

# 인스턴스 생성
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
# print(p.__dict__)
# print(s.__dict__)

p.printInfo()
s.printInfo()
s.working()
s.coding()

