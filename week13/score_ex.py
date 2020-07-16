import score

ban = []

for i in range(5):
    student = []

    name = input("성명 : ")
    korean = int(input("국어 점수 : "))
    english = int(input("영어 점수 : "))
    math = int(input("수학 점수 : "))

    student.append(name)
    student.append(korean)
    student.append(english)
    student.append(math)

    ban.append(student)

# 저장된 5명의 학생의 총점, 평균 학점을 계산 후
# 해당 학생의 리스트에 각 항목을 추가
for i in ban:
    score.total(i)
    score.ave(i)
    score.grade(i)

# 저장된 학생들 모두 출력
for i in ban:
    score.output(i)
print()


print("2명 성적 비교하여 더 좋은 점수의 학생 찾기")
score.output(ban[2])
score.output(ban[4])
print("=== 성적이 더 좋은 학생 === ")
result = score.max_student(ban[2], ban[4])
score.output(result)
print()

print("3명 성적 비교하여 가장 좋은 점수의 학생 찾기")
score.output(ban[1])
score.output(ban[2])
score.output(ban[3])
print("=== 성적이 가장 좋은 학생 === ")
result = score.max_student(ban[1], ban[2], ban[3])
score.output(result)
print()