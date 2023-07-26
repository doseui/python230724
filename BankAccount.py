# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        self.__id = id      # __를 추가하면 외부에서 접근을 못함
        self.__name = name 
        self._balance = balance 
    def deposit(self, amount):
        self._balance += amount 
    def withdraw(self, amount):
        self._balance -= amount
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self._balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)
print(account1)

print("외부에서 접근한 잔액 확인:", account1._balance)  # 단일 밑줄 사용하면 접근은 가능함
# print(globals())