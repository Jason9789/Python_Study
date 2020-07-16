

# 총점
def total(student):
    total_score = 0
    for i in range(1, 4):
        total_score += student[i]

    student.append(total_score)
    return total_score


# 평균
def ave(student):
    total_score = 0
    for i in range(1, 4):
        total_score += student[i]

    average = total_score / 3

    student.append(average)
    return average


# 학점
def grade(student):
    total_score = 0
    for i in range(1, 4):
        total_score += student[i]

    average = total_score / 3

    if average >= 90:
        result = 'A'
    elif average >= 80:
        result = 'B'
    elif average >= 70:
        result = 'C'
    elif average >= 60:
        result = 'D'
    else:
        result = 'F'

    student.append(result)
    return result


def output(student):
    str = "%5s : 국어:%3d 영어:%3d 수학:%3d 총점:%3d 평균:%3.2f 학점: %2s" \
          % (student[0], student[1], student[2], student[3], student[4], student[5], student[6])

    print(str)


# 받은 학생리스트 중 총점이 가장 높은 학생을 리턴
def max_student(*student):
    max_list = []
    max = 0

    for i in student:
        if max <= i[4]:
            max = i[4]
            max_list = i

    return max_list