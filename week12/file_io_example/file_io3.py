

file = open('output/basic.txt', 'a')

str = input("저장할 문자열 입력 : ")
file.write(str)
file.close()

print("저장 되었습니다.")
