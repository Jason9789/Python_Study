print("I eat %d apples." % 3)

print("I eat %s apples." % "five")

number = 3
print("I eat %d apples." % number)

number = 10
day = "three"
print("I ate %d apples. so I was sick %s days" % (number, day))

# % 뒤에 %를 사용하고 싶다면 %%로 쓰면 된다.
print("Error is %d%%" % 98)

# 정렬과 공백
# 오른쪽 정렬 (전체 길이 10)
print("%10s" % "hello")
print("%10s" % "hi")
print("%10s" % "python")

# 왼쪽 정렬
print("%-10s" % "hello")
print("%-10s" % "hi")
print("%-10s" % "python")

# format
print("I eat {} apples".format(3))

number = 10
day = "three"
print("I ate {} apples. so I was sick {} days".format(number, day))

print("I ate {number} apples. so I was sick {day} days".format(number=10, day=3))
