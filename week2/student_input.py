# 슬라이싱 관련 문제.
number = input("학번 : ")
name = input("이름 : ")

str1 = number + name

first = int(input("첫번째 수 : "))
second = int(input("두번째 수 : "))

print(str1[0:])
print(str1[::-1])

print(str1[first:second+1])
