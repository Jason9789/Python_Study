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

# 중위 연산 방식 수식 3개 저장
infix = [
    ['((8-6)*(4+(9/3)))'],
    ['((9*2)-(3*((2+5)/7)))'],
    ['((9*2)-((3*(2+5))/7))']
]
stack = []      # stack list (괄호 및 연산자를 스택에 쌓음)

# 연산자 우선 순위 체크를 위한 값 설정
prio = {}
prio['('] = 0
prio['+'] = 1
prio['-'] = 1
prio['*'] = 2
prio['/'] = 2

for i in infix:
    postfix = []    # postfix로 변환하여 output 저장 후 출력
    test = i        # infix index 값

    j = 0
    while j < len(test[0]):         # 각 인덱스의 길이만큼 반복문 실행
        token = test[0][j]          # 한 글자씩 나누어 무엇인지 체크하기

        if token.isdigit():         # 숫자 체크
            postfix.append(token)

        elif token == '(':          # 열린 괄호 체크
            stack.append(token)

        elif token == ')':          # 닫힌 괄호 체크
            while stack[-1] != '(':         # 스택에 열린 괄호가 있을 때까지
                postfix.append(stack.pop()) # 스택의 연산자를 postfix (output list에 저장)
            if stack[-1] == '(':    # 스택의 마지막 원소가 열힌 괄호일 때
                stack.pop()         # 열린 괄호 없애기

        elif token in '+-*/':           # 연산자 체크
            if len(stack) != 0:         # 스택이 비어있지 않을 때
                if stack[-1] == '(':    # 스택의 top이 열린 괄호이면
                    stack.append(token) # 연산자를 스택에 저장
                else:
                    while prio[token] <= prio[stack[-1]]:   # 연산자 우선순위 비교 후
                        postfix.append(stack.pop())         # 스택에 있는 것을 postfix 리스트에 저장 (output list)
                        if len(stack) == 0: break           # 스택이 비워지면 break
                    stack.append(token)                     # 스택에 연산자 저장
            else:
                postfix.append(token)   # postfix에 연산자 저장
        else:
            postfix.append(token)       # postfix에 연산자 저장

        j += 1

    if len(stack) != 0:                 # 최종적으로 스택이 비워져 있지 않으면
        while len(stack) != 0:          # 스택에 있는 것들을 모두 꺼내 postfix에 저장
            postfix.append(stack.pop())

    print(test[0], "=", "".join(postfix))   # infix와 postfix 출력
