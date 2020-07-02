print('저항 R은 전압 V를 전류 I로 나눈 값이다.')
print('%c = %c / %c' % ('R', 'V', 'I'))

RR = '저항'
VV = '전압'
II = '전류'
print('%s = %s / %s' %(RR, VV, II))

# value -> val
val_V = 1

print(f"\t{RR} R1은 {val_V}/0.4={val_V/0.4}, {RR} R2는 {val_V}/0.2={val_V/0.2}, {RR} R3는 {val_V}/0.1={val_V/0.1}이다.")

print(f"\t3개의 {RR} 중 가장 값이 큰 {RR}은 'R3'라고 할 수 있다.")

print("\t만약 {0} R4가 {3}V의 {1}을 받았을 때 {2}가 0.5A라면, 4V의 {1}을 받았을 때의 {2}는 {R4_A}A일 것이다.".format(RR, VV, II, val_V, R4_A = 4/2))

explain = """엄의 법칙은 전자기학의 가장 기본적인 법칙 중 하나로,
전자의 흐름인 전류는 저항값에 반비례하고 전압에 비례한다는 법칙이다.
독일의 물리학자 엄이 발견해 그의 이름을 따서 만들었다."""

print(explain.count('엄'))
print(explain.find('엄'))
print(explain.index('엄'))

print(explain.replace('엄', '옴'))