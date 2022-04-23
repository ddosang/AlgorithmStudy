n = int(input())
meetings = []
for i in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 여기가 생각하기 어려웠음. 
# 회의 끝나는 시간으로 정렬 후에 하자는거..
meetings.sort(key=lambda x: x[1])

count = 1
end = meetings[0][1]
for i in range(1, n):

    if end <= meetings[i][0]:
        count += 1
        end = meetings[i][1]

print(count)


# 재복습
n = int(input())
interviews = [list(map(int, input().split())) for _ in range(n)]

interviews.sort(key=lambda x: x[1])

count = 1
last_interview = 0

for i in range(1, n):
    if interviews[last_interview][1] <= interviews[i][0]:
        count += 1
        last_interview = i

print(count)
