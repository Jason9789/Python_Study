import calendar

print(calendar.calendar(2020))

year = int(input("년도 입력 : "))
month = int(input("월 입력 : "))
day = int(input("일 입력 : "))
print()

calendar.prmonth(year, month)

result = calendar.weekday(year, month, day)

if result == 0:
    day_result = "월"
elif result == 1:
    day_result = "화"
elif result == 2:
    day_result = "수"
elif result == 3:
    day_result = "목"
elif result == 4:
    day_result = "금"
elif result == 5:
    day_result = "토"
elif result == 6:
    day_result = "일"

print()
print(f"{year}년 {month}월 {day}일 {day_result}요일")
