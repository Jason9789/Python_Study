sum = 0
nineSum = 9
nine = 9

print("====")

while True:
    if sum < 100:
        sum += nineSum

        if sum > 100:
            break

        print("%d + " % nineSum, end='')

        nineSum += nine


print("0 = %d" % sum)

