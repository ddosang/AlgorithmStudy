# 원래 문제에서는 deque 와 pop 을 이용해서 풀었는데,
# deque 구현법을 다시 공부해보자.

n, m = map(int, input().split())
people = list(map(int, input().split()))

people.sort()
left = 0
right = n-1
count = 0

# while left <= right:
#     if people[left] + people[right] <= m:
#         left += 1
#         right -= 1
#     else:
#         right -= 1

#     count += 

# 안되는 케이스 추가

while left <= right:
    if people[left] + people[right] <= m:
        left += 1
        right -= 1
        n -= 2
    else:
        right -= 1
        n -= 1

    count += 1

if n == 1:
    count += 1

print(count)



# 재복습
from collections import deque

n, m = map(int, input().split())
people = list(map(int, input().split()))

people.sort(reverse=True)

people = deque(people)
count = 0
while len(people) > 1:
    if people.popleft() + people[-1] <= m:
        people.pop()

    count += 1

while people:
    people.pop()
    count += 1

print(count)
