

class Student:
    st_count = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Student.st_count += 1

    def output(self):
        print('name : ', self.__name)
        print('age : ', self.__age)

    def get_count(self):
        return Student.st_count

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def compare(s1, s2):
        if s1.get_age() >= s2.get_age():
            return s1
        else:
            return s2


st1 = Student("홍길동", 20)
st2 = Student("이영희", 24)

st1.output()
st2.output()

print("student의 객채 수 : ", st1.get_count())
print("student의 객채 수 : ", st2.get_count())
print("student의 객채 수 : ", st1.st_count)
print("student의 객채 수 : ", Student.st_count)

print("s1과 s2 중 연장자 : ", Student.compare(st1, st2).get_name())
