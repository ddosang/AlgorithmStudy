from itertools import combinations as cb
import sys
input = sys.stdin.readline

while True:
    S = list(map(int, input().split()))
    K = S.pop(0)

    if K == 0:
        break

    for arr in list(a for a in cb(S, 6)):
        for a in arr:
            print(a, end=' ')
        print()
    print()
