

class Student:
    st_count = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Student.st_count += 1

    def __str__(self):
        return 'name : {} age : {}'.format(self.__name, self.__age)

    def output(self):
        print(f"name : {self.__name}")
        print(f"age : {self.__age}")


st1 = Student("홍길동", 20)
st2 = Student("홍길동", 20)

st1.output()
st2.output()

print("st1의 id : ", id(st1))
print("st2의 id : ", id(st2))

if st1 == st2:
    print('st1과 st2가 동일인')
else:
    print('st1과 st2는 다른 인물')

print('str() 호출 1 : ', str(st1))
print('str() 호출 2 : ', str(st2))

