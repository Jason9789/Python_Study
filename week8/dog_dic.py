# 강아지 딕셔너리 생성
dog = []
dog_list = {}

for num in range(3):
    dog_list['name'] = input("강아지 이름 : ")
    dog_list['age'] = int(input("강아지 나이 : "))
    dog_list['king'] = input("강아지 종류 : ")
    dog.append(dict(dog_list))

print("리스트 내용")
for num in range(3):
    print(f"{num} 번째 : ", dog[num])


print("나이가 3살 이상인 강아지")
for i in range(3):
    if dog[i]['age'] >= 3:
        print(dog[i])

