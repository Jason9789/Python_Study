# 날짜/시간과 관련된 기능을 가져온다.
import datetime

# 현재 날짜/시간을 구한다.
now = datetime.datetime.now()

# 출력
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

# 출력
print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

# 오전 오후 구분
if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))

else:
    print("현재 시각은 {}시로 오후입니다!".format(now.hour))