import sys

readl = sys.stdin.readline

def 균형(str):
    cnt = 0

    stack = []

    # 스택에 넣는데,
    for c in str:
        # print(c)
        # ( 이면 그냥 넣고,
        if c == '(':
            stack.append('(')

        # ) 이면
        elif c == ')':
            # 스택안에 ( 가 있으면 pop
            if len(stack) > 0:
                if stack[-1] == '(':
                    stack.pop()

            # 스택에 비어 있으면 잘못 입력한 것이므로 ( 로 바꿔서 넣는다.
            else:
                cnt += 1
                stack.append('(') # ( 로 바꾸기

        # print(stack)

    # 그러면 잘못 입력한 ) 만 ( 로 바꿨기 때문에,
    # ( 을 ) 로 바꿔서 괄호 개수를 맞춰줘야 함.
    # 그 횟수는 (나머지 ( 개수) // 2
    if stack:
        cnt += len(stack) // 2

    return cnt


str = readl()


print(균형(str))
