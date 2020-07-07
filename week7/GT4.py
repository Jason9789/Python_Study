calc = True
PV = 1000
year = 5

while calc:
    base = 1
    k = int(input('수익률을 % 단위로 입력하세요. 종료를 원하시면 음수를 입력합니다: '))

    if k < 0:
        print('종료합니다.')
        calc = False

    else:
        for i in range(year):
            base *= 1 + k / 100

        FV = PV * base
        print('원금이 %d원이고 연 수익률이 %d%%일 때 %d년 후 미래가치는 %.2f원입니다.' % (PV, k, year, FV))

