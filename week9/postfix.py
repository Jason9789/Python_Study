# 스택의 과제
# 중순위와 후순위 방식
# 식 8+9 방식은 연산자가 피연산자 사이에 있는 중순위 방식이다.같은 식에서 연산자를 피연산자 뒤에 적는 방식은 후순위 라고 하며 89+ 와 같다.
# 중순위를 후순위로 변환
# 새로운 빈 문자열 생성 (후순위로 변환될 수식)
# 중순위 수식을 차례로 하나씩 쪼개서
#  ‘(‘, ‘+’, ‘-’, ‘*’, ‘/’ 이면 스택에 저장하고,
# 숫자이면 새로운 문자열로 연결한고 (isdigit() 함수 이용),
# ‘)’ 이면 스택에서  ‘(’ 일 때 까지 하나씩 꺼내 새로운 문자열에 연결하고, 꺼낸 문자가 ‘(‘ 일때는 새로운 문자열에 연결하지 않는다.
# 최종 원래 수식과 변환된 수식을 출력
# 수식3개를 리스트로 만듬
# 식1 : ((8-6)*(4+(9/3)))
# 식2 : ((9*2)-(3*((2+5)/7)))
# 식3 : ((9*2)-((3*(2+5))/7))
# 리스트에서 하나씩 꺼내 후순위로 변환한 후 중순위 방식과 후순위 방식을 출력

infix = [
    ['((8-6)*(4+(9/3)))'],
    ['((9*2)-(3*((2+5)/7)))'],
    ['((9*2)-((3*(2+5))/7))']
]
stack = []      # stack list
# postfix = []    # output

# 연산자 우선 순위 체크
prio = {}
prio['('] = 0
prio['+'] = 1
prio['-'] = 1
prio['*'] = 2
prio['/'] = 2

for i in infix:
    postfix = []    # postfix로 변환하여 output 저장 후 출력
    test = i

    j = 0
    while j < len(test[0]):
        token = test[0][j]

        if token.isdigit():
            postfix.append(token)

        elif token == '(':
            stack.append(token)

        elif token == ')':
            while stack[-1] != '(':
                a = stack.pop()
                postfix.append(a)
            if stack[-1] == '(':
                stack.pop()

        elif token in '+-*/':
            if len(stack) != 0:
                if stack[-1] == '(':
                    stack.append(token)
                else:
                    while prio[token] <= prio[stack[-1]]:
                        postfix.append(stack.pop())
                        if len(stack) == 0: break
                    stack.append(token)
            else:
                postfix.append(token)
        else:
            postfix.append(token)

        j += 1

    if len(stack):
        while len(stack) != 0:
            postfix.append(stack.pop())

    print(test[0], "=", "".join(postfix))
