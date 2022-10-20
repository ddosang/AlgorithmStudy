import sys

n = int(sys.stdin.readline())
arr = [0] * 10001

for i in range(n):
    index = int(sys.stdin.readline())
    arr[index] += 1

for i in range(1, 10001):
    for j in range(arr[i]):
        print(arr[i])
