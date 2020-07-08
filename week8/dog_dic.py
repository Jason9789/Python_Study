# 강아지 딕셔너리 생성
dog_list = []
dog = {}

for num in range(3):
    dog['name'] = input("강아지 이름 : ")
    dog['age'] = int(input("강아지 나이 : "))
    dog['king'] = input("강아지 종류 : ")
    dog_list.append(dict(dog))

print("리스트 내용")
for num in range(len(dog_list)):
    print(f"{num} 번째 : ", dog_list[num])


print("나이가 3살 이상인 강아지")
for dog in dog_list:
    if dog['age'] >= 3:
        print(dog)

