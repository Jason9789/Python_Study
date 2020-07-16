

class BankAccount:
    rate = 0.05

    def __init__(self, name, balance=0):
        self.__name = name
        self.__balance = balance

    def disp(self):
        print(f"name : {self.get_name()} balance : {self.get_balance()}")

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        if self.__balance - money >= 0:
            self.__balance -= money
            return 1
        else:
            return -1

    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    def calcuInterest(self):
        tmp = self.__balance * BankAccount.rate
        self.__balance += int(tmp)


# 객체 생성
person1 = BankAccount("김철수", 30000)
person2 = BankAccount("이영희")

# 객체 정보 출력
person1.disp()
person2.disp()
print("----------------------------")


# 김철수 150000 입금, 50000 출금
print(f"{person1.get_name()} 150,000 입금 / 50,000 출금")
person1.deposit(150000)
print(f"{person1.get_name()} 잔액 : {person1.get_balance()}")

if person1.withdraw(50000) == 1:
    print(f"50000원 출금 잔액 : {person1.get_balance()}")
elif person1.withdraw(50000) == -1:
    print("잔액이 부족")
print("----------------------------")


# 이영희 50000 입금, 100000 출금
print(f"{person2.get_name()} 50,000 입금 / 100,000 출금")
person2.deposit(50000)
print(f"{person2.get_name()} 잔액 : {person2.get_balance()}")

if person2.withdraw(100000) == 1:
    print(f"50000원 출금 잔액 : {person2.get_balance()}")
elif person2.withdraw(100000) == -1:
    print("잔액이 부족")
    print(f"{person2.get_name()} 잔액 : {person2.get_balance()}")
print("----------------------------")


# 이자 계산 전
print("이자 계산 전")
person1.disp()
person2.disp()
print()

# 이자 계산 후
print("이자 계산 후")

person1.calcuInterest()
person2.calcuInterest()

person1.disp()
person2.disp()
