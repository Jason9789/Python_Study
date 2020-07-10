# 딕셔너리를 리턴하는 함수
# 함수 이름 : computing()
# 2개의 정수 값을 매개변수로 가짐
# 키 ‘합’에 두수의 합,  키 ‘차’에 큰 수에서 작은 수의 차, 키 ‘곱’에 두수의 곱,  키
# ‘몫’에 큰 수에서 작은 수의 정수형 몫을 딕셔너리 형태로 만들어 리턴
# 두수를 입력 받음 (0을 입력하면 다시 입력 받음)
# 입력한 두수로 함수 computing 호출함
# 리턴 받은 값을 출력할 때 딕셔너리는 for 문을 이용함
# (출력시 딕셔너리를 하나의 변수로 바로 출력하지 않고 반복문을 이용하여 한 항목씩 출력함 )


def computing(num1, num2):

    # 합
    sum = num1 + num2

    # 곱
    mul = num1 * num2

    # 차 & 나누기
    if num1 < num2:
        sub = num2 - num1
        div = num2 / num1
    else:
        sub = num1 - num2
        div = num1 // num2

    dic = {'합' : sum, '차' : sub, '곱' : mul, '몫' : div}

    for key, value in dic.items():
        print(key, ":", value, " ", end='')


flag = True
while flag:
    num1 = int(input("0이 아닌 정수 입력 : "))
    if num1 == 0:
        continue

    num2 = int(input("0이 아닌 정수 입력 : "))
    if num2 == 0:
        continue

    computing(num1, num2)
    flag = False



