num1 = 4
num2 = 0

print("==============")

for i in range(0, 3):
    num2 = num1

    for j in range(0, 4):
        print(num2, "\t", end='')
        num2 += 1
    print()
    num1 += 1

print("==============")