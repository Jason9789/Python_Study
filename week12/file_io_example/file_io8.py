

print("name     weight     height     BMI        result")
with open("output/info.txt", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break

        (name, weight, height) = line.strip().split(',')
        bmi = int(weight) / ((int(height) / 100) ** 2)

        if bmi >= 25:
            result = "과제중"
        elif bmi >= 18.5:
            result = "보통 체중"
        else:
            result = "저체중"

        print("%-8s %4s       %4s      %5.2f %10s" %(name, weight, height, bmi, result))