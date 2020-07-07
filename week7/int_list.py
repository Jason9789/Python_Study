
arr = []

for i in range(5):
    arr.append(int(input('정수 입력 : ')))

print(arr)
print()

print("max : %d" % max(arr))
print("min : %d" % min(arr))
print("sum : %d" % sum(arr))
print()

print("역순 : ", end='')
arr2 = reversed(arr)

for num in arr2:
    print(num, '', end='')
print('\n')

addNum = int(input('삽입 정수 : '))
addIdx = int(input('삽입할 인덱스 : '))
arr.insert(addIdx, addNum)
print(arr, '\n')


delNum = int(input('삭제할 정수 : '))

if delNum in arr:
    arr.remove(delNum)
    print(arr, '\n')
else:
    print('sorry, not found')
    print(arr, '\n')

print("역순 : ", end='')
arr.reverse()
print(arr)

print("정렬 : ", end='')
arr.sort()
print(arr)


