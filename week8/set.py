
set1 = {'x', 'b', 'g', 'd', 'q'}
set2 = {'b', 'w', 'g', 'q', 'o'}

print("set1 = ", set1)
print("set2 = ", set2)

print('set1 ∪ set2 = ', set1 | set2)
print("set1 ∩ set2 = ", set1 & set2)
print("set1 - set2 = ", set1 - set2)
print("set2 - set1 = ", set2 - set1)
print("set1 ^ set2 = ", set1 ^ set2)
print()

char = input("영문자 한자 입력 : ")

if char in set1:
    print("중복된 입력입니다.")
else:
    set1.add(char)

print("set1 = ", set1)

delChar = input("영문자 한자 입력 : ")
if delChar in set2:
    set2.remove(delChar)

else:
    print("삭제할 문자가 없습니다.")

print("set2 = ", set2)
