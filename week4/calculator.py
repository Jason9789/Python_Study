print("==================")

num1 = input("첫번째 정수 입력 : ")
num2 = input("두번째 정수 입력 : ")

if num1 >= num2:
    result = int(num1) - int(num2)
    print(num1, " - ", num2, " = ", result)

if num2 > num1:
    result = int(num2) - int(num1)
    print(num2, " - ", num1, " = ", result)

print("==================")