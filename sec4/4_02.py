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


k, n = map(int, input().split())
line_lengths = [int(input()) for _ in range(k)]

start = 1
end = max(line_lengths)
max_split_length = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    for line in line_lengths:
        count += line // mid

    if count >= n:
        if max_split_length < mid:
            max_split_length = mid
        start = mid + 1
    else:
        end = mid - 1


print(max_split_length)

