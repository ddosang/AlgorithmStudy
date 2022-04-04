import sys
sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())

lans = []
possible = []
for i in range(n):
    lans.append(int(input()))

lans.sort()
length = lans[-1]
while length > 0:
    length //= 2
    count = 0
    for lan in lans:
        count += lan // length

    if count == k:
        possible.append(length)

print(max(possible))
