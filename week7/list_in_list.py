
arr = [
    ['A', 80, 80, 80],
    ['A', 90, 90, 90],
    ['B', 60, 70, 80],
    ['A', 71, 78, 77],
    ['B', 70, 80, 73],
    ['B', 90, 87, 92]
]

litA = []
litB = []


for i in range(len(arr)):
    total = 0
    for j in range(1, 4):
        total += arr[i][j]

    ave = round(total / 3, 1)
    arr[i].append(ave)

for i in range(len(arr)):
    if arr[i][0] == 'A':
        litA.append(arr[i][4])

    elif arr[i][0] == 'B':
        litB.append(arr[i][4])

print("========================")
print("A : ", litA)
print("B : ", litB)
print("reversed()로 역순출력")

revA = reversed(litA)
revB = reversed(litB)

print("A 역순 : ", end='')
for num in revA:
    print(num, '', end='')
print()

print("A 역순 : ", end='')
for num in revB:
    print(num, '', end='')
print()
print("========================")
