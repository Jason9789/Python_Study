

def maxFunc(A):
	max = 0
	for i in range(len(A)):
		if max < A[i]:
			max = A[i]
	return max


A = [1, 2, 3, 4, 5, 6, 73, 8, 10, 54]

maxNum = maxFunc(A)
print(maxNum)