import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    n = int(readl())
    list_cmd = [list(readl().split()) for _ in range(N)]
    return n, list_cmd


def solution():
    stack = deque()
    for cmd in list_cmd:
        if cmd[0] == 'o':
            if len(stack) > 0:
                print(stack.pop())
            else:
                print("empty")

        elif cmd[0] == 'i':
            stack.append(cmd[1])
            # stack.push(cmd[1])
        elif cmd[0] == 'c':
            print(len(stack))



n, list_cmd = Input_Data()
solution()
