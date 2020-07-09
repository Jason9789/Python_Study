# 큐 과제
# 과일 목록을 큐에 저장하고 삭제
# 초기 메뉴에서 삽입/삭제/종료 선택
# 종료시 프로그램 종료
# 삽입
# 과일 이름 입력받음
# 큐에 삽입 append() 이용
# 큐 출력
# 삭제
# 큐에서 과일 삭제 pop() 이용

queue = []
flag = True

while flag:
    keyWord = input('삽입/삭제/종료 : ')

    if keyWord == '종료':
        flag = False

    elif keyWord == '삽입':
        fruit = input("과일 이름 : ")
        queue.append(fruit)
        print(queue)

    elif keyWord == '삭제':
        num = len(queue)
        if num == 0:
            print("삭제할 과일이 없습니다!!!")
            continue
        else:
            fruit = queue.pop(0)
            print("삭제된 과일 : %s" % fruit)
            print(queue)

    else:
        print("잘못 입력하였습니다!!!")

