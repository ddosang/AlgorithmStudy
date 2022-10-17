import sys
from collections import deque

# 스택에 들어갈 때 비교하는 우선순위
def input_priority(str):
    if str == "(":
        return 4
    if str == "*" or str == "/":
        return 3
    elif str == "+" or str == "-":
        return 2
    elif str == "(":
        return 1
    return 0

# 스택에 들어가있는 녀석을 비교하는 우선순위
def output_priority(str):
    if str == "(":
        return 0
    if str == "*" or str == "/":
        return 3
    elif str == "+" or str == "-":
        return 2
    return 0

str_exp = sys.stdin.readline()[:-1]

computes = []
stack = deque()

# 후위표기식으로 변경
for c in str_exp:
    if c.isdecimal():
        computes.append(c)
    else:
        if len(stack) == 0:
            stack.append(c)
        else:
            if output_priority(stack[-1]) < input_priority(c):
                stack.append(c)
            else:
                if c == ')':
                    while stack and stack[-1] != '(':
                        computes.append(stack.pop())
                    stack.pop() # ( 를 삭제.
                else:
                    while stack and output_priority(stack[-1]) >= input_priority(c):
                        computes.append(stack.pop())
                    stack.append(c)

while stack:
    computes.append(stack.pop())

print(computes)

# 후위표기식 계산
for c in computes:
    if c.isdecimal():
        stack.append(c)
    else:
        n2 = int(stack.pop())
        n1 = int(stack.pop())
        if c == "+":
            stack.append(n1 + n2)
        elif c == "-":
            stack.append(n1 - n2)
        elif c == "*":
            stack.append(n1 * n2)
        elif c == "/":
            stack.append(int(n1 / n2))

print(stack[0])
