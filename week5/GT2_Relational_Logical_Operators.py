num = int(input())

if num <= -10 or num >= 10:
	print("1점입니다.")
elif num <= -7 or num >= 7:
	print("2점입니다.")
elif num <= -3 or num >= 3:
	print("3점입니다.")
elif num <= -1 or num >= 1:
	print("4점입니다.")
elif num == 0:
	print("축하합니다! 5점입니다.")
else:
	print("점수를 출력할 수 없습니다.")

