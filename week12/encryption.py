

key = 'abcdefghijklmnopqrstuvwxyz'

file = open("encryption_file.txt", "w")


def encrypt(origin):
    for i in origin:
        find_key = key.find(i)
        # print(find_key)
        if find_key + 2 <= 25:
            i = key[find_key + 2]
        else:
            i = key[find_key - 24]
            # print(i)
        file.write(i)
    file.write('\n')

def decrypt(encryption):
    str = ""
    for i in encryption:
        find_key = key.find(i)
        i = key[find_key - 2]
        str += i

    return str

for i in range(3):
    original = input("문자열 입력 (대문자, 빈칸, 특수기호 불가) : ")
    encrypt(original)

print("암호 저장 완료!!!")
file.close()

with open("encryption_file.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        print(f"암호 : {line}")
        result = decrypt(line)
        print(f"해독 : {result}")