

def calNums(base, *nums):
    for i in nums:
        total = 1
        for j in range(i):
            total *= base
        print(f'{base}의 {i} 제곱 값은 {total}이다.')


calNums(5, 1, 2, 3)
calNums(2, 2, 4, 6, 8, 10)
