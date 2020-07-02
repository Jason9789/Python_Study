str = "안녕안녕하시오"

print(str.find('안녕'))
print(str.rfind('안녕'))
print(str.count('안녕'))


ss = "Hello Python 3.8"
tt = ss.split(' ')
s1 = tt[0]
s2 = tt[1]
s3 = tt[2]

print('tt : ', tt)
print('s1 : ', s1, ' s2 : ', s2, ' s3 : ', s3)

s4 = float(s3)
print('s3 type : ', type(s3))
print('s4 type : ', type(s4))

str2 = 'The girl is nicce!'
print(str2)

print(str2.replace('girl', 'boy'))

list01 = ['드럼', '기타', '베이스', '키보드']

print(list01)
print(' '.join(list01))
print(', '.join(list01))
print(' / '.join(list01))


