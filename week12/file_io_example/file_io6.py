

with open("output/info.txt", "w") as file:
    for i in range(5):
        name = input("이름 입력 : ")
        weight = input("몸무게 입력 : ")
        height = input("키 입력 : ")

        file.write("%s, %s, %s \n" %(name, weight, height))