import sys

readl = sys.stdin.readline

n, p = map(int, readl().split())

sol = 0
arr = []

temp = n
i = 0
while True:
    temp = temp * n % p
    if temp in arr:
        sol = i - arr.index(temp)
        break
    arr.append(temp)
    i += 1


print(sol)
