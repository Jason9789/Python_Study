

# 3. 가변 매개변수 함수
# 함수 이름 : find_max()
# 여러 개의 숫자에서 가장 큰 값을 리턴하는 함수
# 숫자 여러 개를 매개변수로 가짐
# 가장 큰 수를 찾아 리턴함
# (max() 함수 사용하지 않음)
#
# 숫자를 5개를 입력 받음 (num1~num5)
# find_max() 실행하여 결과값 찾고 출력
# find_max(num1) 실행하여 결과값 찾고 출력
# find_max(num1, num2) 실행하여 결과값 찾고 출력
# 3,4,5 개의 매개변수를 가지고 실행하여 출력

num_list = []


def find_max(*values):
    max = 0
    str = ''

    n = len(values)
    for i in range(n):
        if max < values[i]:
            max = values[i]
        print("%d, " % values[i], end='')
    print("max = %d" % max)


for i in range(5):
    num = int(input("정수 입력 : "))
    num_list.append(num)


find_max()
find_max(num_list[0])
find_max(num_list[0], num_list[1])
find_max(num_list[0], num_list[1], num_list[2])
find_max(num_list[0], num_list[1], num_list[2], num_list[3])
find_max(num_list[0], num_list[1], num_list[2], num_list[3], num_list[4])

