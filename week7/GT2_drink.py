drink = 3

while True:
    money = int(input("돈을 넣어 주세요: "))

    if drink == 0:
        print("음료가 다 떨어져서 영업이 종료되었습니다.")
        break;

    if money == 300:
        print("음료 나왔습니다.")
        drink = drink - 1
    elif money > 300:
        print("거스름돈 %d원과 음료 나왔습니다." % (money - 300))
        drink = drink - 1
    elif money < 300:
        print("잔액이 부족합니다.")
        print("남은 음료 갯수는 %d개 입니다." % drink)
