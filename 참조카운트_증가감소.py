class MyClass:
    # 초기화 메서드
    def __init__(self, value):
        self.Value = value 
        print("Instance is created! Value = ", value)
    # 소멸자 메서드    
    def __del__(self):
        print("Instance is deleted!")
        


c = MyClass(10)
# c_copy = c
# 언젠가 가비지 컬렉션
# del c 
# del c_copy

print("전체 코드 종료")
