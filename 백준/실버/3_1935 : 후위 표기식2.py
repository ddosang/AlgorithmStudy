def calculate(first, second, op):
    if op == "+":
        return first + second
    elif op == "-":
        return first - second
    elif op == "*":
        return first * second
    elif op == "/":
        return first / second



n = int(input())
str = input()
maparr = [int(input()) for _ in range(n)]

stack = []

for s in str:
    if s.isalpha():
        num = maparr[ord(s) - ord('A')]
        stack.append(num)
    else:
        second = stack.pop()
        first = stack.pop()
        c = calculate(first, second, s)
        stack.append(c)

print("{:.2f}".format(stack[-1]))
