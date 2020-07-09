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
postfix = []

test = ['((8-6)*(4+(9/3)))']
test2 = []
stack = []

# print(len(test[0]))

prio = {}
prio['('] = 0
prio['+'] = 1
prio['-'] = 1
prio['*'] = 2
prio['/'] = 2

i = 0
while i < len(test[0]):
    # print(test[0][i])
    token = test[0][i]
    # 숫자일 경우 output에 바로 저장
    if token.isdigit():
        test2.append(token)

    # 기호일 경우
    elif token == '(':
        stack.append(token)
        print(stack[-1])
        # print(len(stack))
        print(stack)

    elif token == ')':
        # print(stack)
        # check = stack.pop()
        # 기호가 ( 가 아니면 꺼낸 기호를 다시 stack에 넣는다.
        # python에는 top이 없기 때문에 [-1]로 top을 체크한다.
        while stack[-1] != '(':
            test2.append(stack.pop())
        if stack[-1] == '(':
            stack.pop()

    elif token in '+-*/':
        if len(stack) != 0:
            print(len(stack))
            # check = stack.pop()

            if stack[-1] == '(':
                stack.append(token)
            else:
                # stack.append(check)
                # print(stack)
                # print(check)
                while prio[token] <= prio[stack[-1]]:
                    test2.append(stack.pop())
                    # test2.append(check)
                    if len(stack) == 0: break
                stack.append(token)
                # test2.append(token)
        else:
            stack.append(token)
    #         test2.append(token)
    else:
    #     stack.append(token)
        test2.append(token)

    i += 1

if len(stack) != 0:
    while len(stack) != 0:
        test2.append(stack.pop())

print("\n===================")
# print(test)
print(test2)
print(stack)
# print(len(stack))
