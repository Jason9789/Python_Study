

class BankAccount:

    def __init__(self, name, number, balance=0):
        self.__name = name
        self.__number = number
        self.__balance = balance

    def disp(self):
        return f"name : {self.get_name()} number : {self.get_number()} balance : {self.get_balance()}"

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

    def get_number(self):
        return self.__number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance


# 저축 예금
class SavingAccount(BankAccount):
    # 객체 갯수
    __counter = 0
    counter = 0
    passbook_number = ""

    def __init__(self, name, balance, rate):
        super().__init__(name, self.get_number(), balance)
        self.__rate = rate
        self.__counter = SavingAccount.counter + 1
        SavingAccount.counter += 1

    def disp(self):
        return f"name : {self.get_name()} number : {self.get_number()} balance : {self.get_balance()} interest : {self.get_rate()}"

    def get_number(self):
        passbook_number = "01-" + "%03d" % self.__counter
        return passbook_number

    def get_rate(self):
        return self.__rate

    # 이자 계산 함수
    def cal_interest(self):
        tmp = self.get_balance() * self.__rate
        self.set_balance(self.get_balance() + int(tmp))


# # 당좌 예금
class CheckingAccount(BankAccount):
    __counter = 0
    counter = 0
    passbook_number = ""

    def __init__(self, name, balance, fee):
        super().__init__(name, self.get_number(), balance)
        self.__fee = fee
        self.__counter = CheckingAccount.counter + 1
        CheckingAccount.counter += 1

    def disp(self):
        return f"name : {self.get_name()} number : {self.get_number()} balance : {self.get_balance()} fee : {self.get_fee()}"

    def get_number(self):
        passbook_number = "02-" + "%03d" % CheckingAccount.counter
        return passbook_number

    def get_fee(self):
        return self.__fee

    def issue_check(self, money):
        if self.get_balance() - self.__fee >= money:
            self.set_balance(self.get_balance() - self.__fee - money)
            return 1
        else:
            return -1


def main():
    account = []

    print("-" * 60)
    p1 = SavingAccount("김철수", 10000, 0.05)
    p2 = SavingAccount("이영희", 200000, 0.03)
    p3 = CheckingAccount("홍길동", 2000000, 30000)

    account.append(p1)
    account.append(p2)
    account.append(p3)

    print("김철수, 이영희, 홍길동 통장 출력")

    for i in account:
        print(i.disp())

    # 김철수 50,000 입금 / 100,000 출금
    print("-" * 60)
    print("김철수 50,000 입금 / 100,000 출금")
    account[0].deposit(50000)
    print(account[0].disp())

    if account[0].withdraw(100000) == 1:
        print(account[0].disp())
    else:
        print("잔액이 부족합니다.")
        print(account[0].disp())

    # 이영희 100,000 입금 / 75,000 출금
    print("-" * 60)
    print("이영희 100,000 입금 / 75,000 출금")
    account[1].deposit(100000)
    print(account[1].disp())

    if account[1].withdraw(75000) == 1:
        print(account[1].disp())
    else:
        print("잔액이 부족합니다.")
        print(account[1].disp())

    # 홍길동 500,000 입금
    print("-" * 60)
    print("홍길동 500,000 입금")
    account[2].deposit(500000)
    print(account[2].disp())

    # 이자 지급 / 당좌수표 발행
    print("-" * 60)
    print("계산 전")
    for i in account:
        print(i.disp())

    print("\n계산 후")

    for i in account:
        # account 의 종류가 SavingAccount 인지 CheckingAccount 인지 확인
        if isinstance(i, SavingAccount):
            i.cal_interest()    # 이자 계산
            print(i.disp())

        elif isinstance(i, CheckingAccount):
            if i.issue_check(1000000) == 1:
                print(i.disp())
            else:
                print("잔액이 부족합니다")
                print(i.disp())




main()