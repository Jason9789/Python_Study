# test.py
import computing

num1 = int(input("정수 입력 : "))
num2 = int(input("정수 입력 : "))

r1 = computing.plus(num1, num2)
r2 = computing.minus(num1, num2)
r3 = computing.multiply(num1, num2)
r4 = computing.divide(num1, num2)

print(r1, r2, r3, r4)