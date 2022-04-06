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
