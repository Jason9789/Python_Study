song = '''
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산
대한사람 대한으로 길이 보전하세
'''

print("=========================")
print(song)
print("=========================")
print()

print('"대한"은 몇번 등장 : ', song.count('대한'))
print('"동해"의 인덱스 : ', song.find('동해'))
print('"사랑"의 인덱스 : ', song.find('사랑'))

print()
print("=========================")

song = song.replace("동해", "남해").replace("백두산", "한라산")
print(song)
print("=========================")

song = song.strip()
print(song)
print("=========================")
print()

song_list = song.split("\n")
print(song_list)
print()
print("=========================")
print()

print('\n'.join(song_list))

print()
print("=========================")
