infix = [
    ['((8-6)*(4+(9/3)))'],
    ['((9*2)-(3*((2+5)/7)))'],
    ['((9*2)-((3*(2+5))/7))']
]

test = ['((8-6)*(4+(9/3)))']
stack = []
out = []

prio = {}
prio['('] = 0
prio['+'] = 1
prio['-'] = 1
prio['*'] = 2
prio['/'] = 2


print("======= test1 =========")

# infix 출력 하는 테스트 코드
i = 0
while i < len(infix):
    j = 0
    while j < len(infix[i]):
        print(infix[i][j], end='')
        j += 1
    print()
    i += 1

print("======= test2 =========")

# infix 출력 하는 테스트 코드2
i = 0
while i < len(infix):
    text = infix[i]
    print(text)
    j = 0
    while j < len(text):
        # print(len(text[i]))
        # print(text[i])
        j += 1
    i += 1

print("======= test3 =========")

i = 0
for i in infix:
    # print(i)
    test = i
    print(test)
    print(test[0])
    print(len(test[0]))
    j = 0
    while j < len(test[0]):
        print(test[0][j], " ", end="")
        j += 1
    print()

print("======= all : test =========")
# 전체 코드 _ 테스트
i = 0
for i in infix:
    out = []
    test = i

    j = 0
    while j < len(test[0]):
        token = test[0][j]

        if token.isdigit():
            out.append(token)

        elif token == '(':
            stack.append(token)
            # print(stack)

        elif token == ')':
            while stack[-1] != '(':
                a = stack.pop()
                out.append(a)
            if stack[-1] == '(':
                stack.pop()
            # stack.append(token)
            # print(stack)

        elif token in '+-*/':
            if len(stack) != 0:
                if stack[-1] == '(':
                    stack.append(token)
                else:
                    while prio[token] <= prio[stack[-1]]:
                        out.append(stack.pop())
                        if len(stack) == 0: break
                    stack.append(token)
            else:
                out.append(token)
        else:
            out.append(token)

        j += 1

    if len(stack):
        while len(stack) != 0:
            out.append(stack.pop())

    print(test[0], "=", "".join(out))
    # print()


# print("======= all =========")
# # 전체 코드 _ 테스트
# j = 0
# while j < len(test[0]):
#     token = test[0][j]
#
#     if token.isdigit():
#         out.append(token)
#
#     elif token == '(':
#         stack.append(token)
#         # print(stack)
#
#     elif token == ')':
#         while stack[-1] != '(':
#             a = stack.pop()
#             out.append(a)
#         if stack[-1] == '(':
#             stack.pop()
#         # stack.append(token)
#         # print(stack)
#
#     elif token in '+-*/':
#         if len(stack) != 0:
#             if stack[-1] == '(':
#                 stack.append(token)
#             else:
#                 while prio[token] <= prio[stack[-1]]:
#                     out.append(stack.pop())
#                     if len(stack) == 0: break
#                 stack.append(token)
#         else:
#             out.append(token)
#     else:
#         out.append(token)
#
#     j += 1



# if len(stack):
#     while len(stack) != 0:
#         out.append(stack.pop())

# print()
# print("======================")
# # print(test)
# # print(stack)
# print("".join(out))