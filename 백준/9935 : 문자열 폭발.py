import sys

readl = sys.stdin.readline

str = readl().rstrip()
pat = readl().rstrip()


stack = []
for i, s in enumerate(list(str)):
    stack.append(s)
    if ''.join(stack[-len(pat):]) == pat:
        for _ in range(len(pat)):
            stack.pop()



print(''.join(stack) if len(stack) else "FRULA")
