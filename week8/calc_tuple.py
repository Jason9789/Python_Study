# 기본 튜플 값
t1 = ('a', (15, 27), 'Program', [-100, 56.432], 'computer')

print("t1의 자료형 : ", type(t1))
print("t1 출력 : ", t1)
print()

t2 = t1[1:4]
print("t2 출력 : ", t2)

t3, t4 = t1[2], t1[4]

print("t3 출력 :  ", t3)
print("t4 출력 :  ", t4)
