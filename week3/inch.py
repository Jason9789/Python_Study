inch = float(input("inch 입력 : "))
cm = inch * 2.54

number = 201603019
name = "pangeun"

print("학번 : %20d" % number)
print("이름 : %20s" % name)


print("==========================")
print("     {:08.2f}".format(inch) + " inch")
print("     {:08.2f}".format(cm) + " cm")
print("==========================")

