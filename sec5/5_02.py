brackets = input()

stack = []
answer = 0

brackets = list(brackets)

for i in range(len(brackets)):
    bracket = brackets[i]

    if bracket == "(":
        stack.append("(")
    else:
        if stack and stack[-1] == "(":
            stack.pop()
            if i > 0:
                answer += len(stack) if brackets[i-1] == "(" else 1
    print(stack, answer)

print(answer)

# ()(((()())(())()))(())
# (((()(()()))(())()))(()())
