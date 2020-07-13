bin_list = []
cnt = 0


def binary(num):
    global cnt
    if num < 0:
        exit()

    elif num == 0:
        bin_list.append(str(0))
        cnt += 1

    elif num >= 1:
        remainder = int(num) % 2
        bin_list.append(str(remainder))
        cnt += 1
        binary(num/2)


num = int(input("양의 정수 입력(음수 입력 시 종료) : "))

binary(num)
bin_list.reverse()
list2bin = "".join(bin_list)

print(f"{num} 의 이진수 : {list2bin}, binary() 함수 반복 횟수 : {cnt}")

