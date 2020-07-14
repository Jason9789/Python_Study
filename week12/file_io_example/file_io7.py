

with open('output/info.txt', 'r') as file:
    line = file.read()
    print(line)




with open('output/info.txt', 'r') as file2:
    lines = file2.readlines()
    print(lines)



with open('output/info.txt', 'r') as file3:
    lines = file3.readlines()

    for line in lines:
        print(line)

