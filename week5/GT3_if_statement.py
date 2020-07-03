num = int(input())


if num <= 0:
	print("자연수가 아닙니다.")
elif num % 2 == 1:
	print("입력한 수 %d는 홀수입니다." %(num))
elif num % 2 == 0:
	print("입력한 수 %d는 짝수입니다." %(num))

