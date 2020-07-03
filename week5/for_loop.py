for i in range(5):
    print(str(i) + " = 반복 변수")

print()

for i in range(5, 10):
    print(str(i) + " = 반복 변수")

print()

for i in range(0, 10, 3):
    print(str(i) + " = 반복 변수")

print()

print("===================")
sum = 0
for i in range(1, 11):
    sum += i

print(f"1부터 10까지의 합 : {sum}")

print("===================")

sum = 0
sum_str = ''
for i in range(1, 11):
    sum += i

    if i < 10:
        sum_str += str(i) + ' + '
    else:
        sum_str += str(i)


print(f"{sum_str} = {sum}")
print("===================")

# 역반복문
for i in range(4, 0 - 1, -1):
    print("현재 반복 변수 : {}".format(i))

print("===================")

for i in reversed(range(5)):
    print("현재 반복 변수 : {}".format(i))

print("===================")

# continue
for i in range(10):
    if i <= 5:
        continue
    print(f"{i} > 5")

print("===================")

sum = 0
for i in range(10):
    if i % 2 == 0:
        continue
    else:
        sum += i

print(f"홀수의 합 : {sum}")

print("===================")
num = 1
for i in range(3):
    for j in range(5):
        print("{:3} ".format(num), end='')
        num += 1
    print()

print("===================")
# 구구단
for i in range (1, 10):
    for j in range(2, 5):
        print("{:3} *{:3} = {:3}".format(j, i, j*i), end='')
    print()

