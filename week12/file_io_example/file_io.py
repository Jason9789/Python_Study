

myfile = open('out.txt', 'w')

for i in range(5):
    num = input("정수 입력 : ")
    myfile.write(num)

myfile.close()
print('프로그램 종료')