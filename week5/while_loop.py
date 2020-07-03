import time

sum = 0
print('1부터 10까지의 합')

i = 1
while i <= 10:
    sum += i

    if i < 10 :
        print(i, '+ ', end='')
    else:
        print(i, '= ', end='')
    i += 1

print(sum)


number = 0

# 5초 동안 반복합니다.
# target_tick = time.time() + 5
# while time.time() < target_tick:
#     number += 1

# print("5초 동안 {}번 반복했습니다.".format(number))

print("============================")
str1 = input("문자열 입력 : ")
num = len(str1)

for i in range(0, num):
    print(str1[i], ' ', end='')
print()

i = -1
while i >= -num:
    print(str1[i], ' ', end='')
    i -= 1
print()

print("============================")

calc = True
while calc:
    fib1 = 1
    fib2 = 1

    num = int(input("피보나치 수열의 순서를 입력 (종료시 0 입력) : "))

    if num == 0:
        calc = False

    else:
        for i in range(1, num+1):
            if i == 1:
                print("{} ".format(fib1), end='')
            elif i == 2:
                print("{} ".format(fib2), end='')
            else:
                print("{} ".format(fib1 + fib2), end='')
                temp = fib1 + fib2
                fib1 = fib2
                fib2 = temp
        print()