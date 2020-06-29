# string formatting

age = int(input("나이 : "))
name = input("이름 : ")

current_year = int("2020")
birth_year = current_year - age + 1

print("당신의 출생년도는 %d 입니다." % birth_year)
print("당신의 이름은 %s 입니다." % name)
