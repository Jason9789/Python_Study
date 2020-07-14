cnt = 0

song = ['동해물과 백두산이 마르고 닳도록\n',
        '하느님이 보우하사 우리나라 만세\n',
        '무궁화 삼천리 화려강산\n',
        '대한사람 대한으로 길이보전하세\n'
        ]

# 파일 쓰기
file = open('song.txt', 'w')
file.writelines(song)

# 파일 읽기
file = open('song.txt', 'r')
lines = file.readlines()

for line in lines:
    line = line.strip()
    result = line.split()
    for i in range(len(result)):
        cnt += 1
    print(line)
    # print(cnt)

print("단어의 수 : %d" % cnt)
print()

# 줄 번호 매기기
line_cnt = 1
new_file = open('new_song.txt', 'w')

for line in lines:
    line = line.strip()
    str = f"{line_cnt} : {line}\n"

    new_file = open('new_song.txt', 'a')
    new_file.writelines(str)
    line_cnt += 1

# 새로운 파일 열기
new_file = open('new_song.txt', 'r')
lines = new_file.readlines()

for line in lines:
    line = line.strip()
    print(line)
