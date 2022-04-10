# 원래 문제에서는 deque 와 pop 을 이용해서 풀었는데,
# deque 구현법을 다시 공부해보자.

n, m = map(int, input().split())
people = list(map(int, input().split()))

people.sort()
left = 0
right = n-1
count = 0

while left <= right:
    if people[left] + people[right] <= m:
        left += 1
        right -= 1
    else:
        right -= 1

    count += 1

print(count)
