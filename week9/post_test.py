test = ['((8-6)*(4+(9/3)))']
stack = []
out = []

prio = {}
prio['('] = 0
prio['+'] = 1
prio['-'] = 1
prio['*'] = 2
prio['/'] = 2

i = 0
while i < len(test[0]):
    token = test[0][i]

    if token.isdigit():
        out.append(token)

    elif token == '(':
        stack.append(token)
        print(stack)

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

    i += 1

if len(stack):
    while len(stack) != 0:
        out.append(stack.pop())

print()
print("======================")
print(test)
print(stack)
print(out)