
song = ['동해물과 백두산이 마르고 닳도록\n',
        '하느님이 보우하사 우리나라 만세\n',
        '무궁화 삼천리 화려강산\n',
        '대한사람 대한으로 길이보전하세\n'
        ]

# 파일 쓰기
with open('song.txt', 'w') as write_file:
    write_file.writelines(song)

# song.txt 파일 읽기
read_file = open('song.txt', 'r')
lines = read_file.readlines()

cnt = 0
for line in lines:
    line = line.strip()

    # 단어 수 증가
    result = line.split()
    for i in range(len(result)):
        cnt += 1
    print(line)

print("단어의 수 : %d" % cnt)
print()

# 줄 번호 매기기
line_cnt = 1

# new_song.txt 만들기
# 새로 만들지 않으면 프로그램 실행을 할 때마다
# 뒤에 있는 open('new_song.txt', 'a') 때문에 이어서 써짐
new_file = open('new_song.txt', 'w')
new_file.close()

# 여기서 lines는 위에 있는 read_file의 lines임
for line in lines:
    line = line.strip()
    str = f"{line_cnt} : {line}\n"

    # 새로운 파일에 쓰기
    # 한 줄씩 new_song.txt 에 이어서 write 한다.
    new_file = open('new_song.txt', 'a')
    new_file.writelines(str)
    new_file.close()

    # 라인 수 증가
    line_cnt += 1

# song.txt 닫기
read_file.close()

# 새로운 파일 열기 및 출력하기
with open('new_song.txt', 'r') as new_file:
    lines = new_file.readlines()

    for line in lines:
        line = line.strip()
        print(line)
