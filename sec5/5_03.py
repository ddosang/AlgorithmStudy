expression = input()

expression = list(expression)

num_stack = []
op_stack = []
answer = ""
priority = {"(" : 4, "*" : 2, "/" : 2, "+" : 1, "-" : 1}
pop_priority = {"(" : 0, "*" : 2, "/" : 2, "+" : 1, "-" : 1}
p = 0
for exp in expression:
    if exp.isdigit():
        num_stack.append(exp)
        answer += exp

    elif exp == ")":
            while op_stack and op_stack[-1] != "(":
                answer += op_stack.pop()
            if op_stack and op_stack[-1] == "(":
                op_stack.pop()

    else:
        if priority[exp] > p:
            op_stack.append(exp)
        else:
            while op_stack and pop_priority[op_stack[-1]] >= priority[exp]: # 다른데서 놓친 줄 알았는데 priority[exp] 대신 p를 써서 이상하게 나오는 거였음.
                answer += op_stack.pop()
            op_stack.append(exp)
        p = priority[exp]

    print(op_stack)

while op_stack:
    answer += op_stack.pop()

print(answer)


# 3+5*2/(7-2)
# 3*(5+2)-9
