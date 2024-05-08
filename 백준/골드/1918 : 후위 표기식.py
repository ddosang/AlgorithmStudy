def priority(s):
    if s == "(":
        return 3
    elif s == "*" or s == "/":
        return 2
    elif s == "+" or s == "-":
        return 1
    else:
        return 0
# priority 를 제대로 쓰고 싶으면
# input priority 는 위의 걸로
# output priority 는 "(" 를 제일 낮게 수정해야함.


string = input()
result = ""
n_stack = []
stack = []

for s in string:
    if s.isalpha():
        result += s
    elif s == "(":
        stack.append(s)
    elif s == ")":
        while stack and stack[-1] != "(":
            result += stack.pop()
        stack.pop()
    else:
        while stack and priority(s) <= priority(stack[-1]):
            if stack[-1] == "(":
                break
            result += stack.pop()
          
        stack.append(s)
            
while stack:
    top = stack.pop()
    if top == "(" or top == ")":
        continue
    result += top

print(result)
