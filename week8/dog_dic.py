dog_list = []

for num in range(3):
    dog_dict = {}

    dog_dict['name'] = input("강아지 이름 : ")
    dog_dict['age'] = int(input("강아지 나이 : "))
    dog_dict['king'] = input("강아지 종류 : ")
    dog_list.append(dict(dog_dict))

print("리스트 내용")
for num in range(len(dog_list)):
    print(f"{num} 번째 : ", dog_list[num])


print("나이가 3살 이상인 강아지")
for dog_dict in dog_list:
    if dog_dict['age'] >= 3:
        print(dog_dict)

