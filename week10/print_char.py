
# 특수 문자 인쇄
# 함수 : 특수 문자를 행의 번호만큼 입력
# 매개변수1 : 출력할 특수 문자
# 매개변수2 : 출력할 라인 수

# SC = special Character (특수 문자)
# num = 라인 수
def print_char(SC, num):
    for i in range(num):
        for j in range(num - i):
            print("=", end='')
        for j in range(i + 1):
            print(SC, end='')
        print()


print_char("&", 5)
print_char("&", 10)

# chara = input("특수 : ")
# num = int(input("라인 : "))
# for i in range(num + 1):
#     for j in range(num - i + 1):
#         print("=", end='')
#     for j in range(i):
#         print(chara, end='')
#     print()