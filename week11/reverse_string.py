def reverse_string(original, i):
    if -len(original) > i:
        return

    else:
        print(original[i], end='')
        reverse_string(original, i-1)


original = input("문자열 입력 : ")
reverse_string(original, -1)
