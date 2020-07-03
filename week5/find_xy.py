# xy (x**y) 값 구하기

base = int(input("정수 입력 : "))
power = int(input("정수 입력 : "))

result = 1

for i in range(1, power + 1):
    result *= base

    if i < power:
        print(f"{base} * ", end='')

    else:
        print(f"{base} = {result}")

