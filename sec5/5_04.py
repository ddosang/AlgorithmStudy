expression = input()
expression = list(expression)

num_stack = []

for exp in expression:
    if exp.isdigit():
        exp = int(exp)
        num_stack.append(exp)
    else:
        second = num_stack.pop()
        first = num_stack.pop()
        if exp == "+":
            num_stack.append(first + second)
        elif exp == "-":
            num_stack.append(first - second)
        if exp == "*":
            num_stack.append(first * second)
        if exp == "/":
            num_stack.append(first / second)

print(num_stack[0])
