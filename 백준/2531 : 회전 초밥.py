import sys
readl = sys.stdin.readline

n, d, k, c = map(int, readl().split())
sushi = [int(readl()) for _ in range(n)]

ch = {}

for s in sushi:
    ch[s] = 0

ch[c] = 0

sushi += sushi[0 : k] # 회전인데 그거 % 하기 귀찮으니 먹을 접시 수 -1 만큼 뒤로 붙인다.


sol = 0

for s in sushi[0:k]:
    ch[s] += 1

종류 = len(set(sushi[0:k])) # 0 ~ k

# print(sushi[0:k])
existC = 0
for i in range(n):
    # if len(set(sushi[i:i+k] + [c])) > sol:
    #     sol = len(set(sushi[i:i+k] + [c]))

    ch[sushi[i]] -= 1 # 왼쪽 빼고,
    if ch[sushi[i]] == 0: # 왼쪽 종류가 이제 없어졌다면.
        종류 -= 1

    if ch[sushi[i + k]] == 0: # 오른쪽 넣을게 원래 없었다면
        종류 += 1
    ch[sushi[i + k]] += 1 # 오른쪽 넣고


    # 쿠폰 초밥이 없다면 해당 초밥도 더해야함.
    if ch[c] == 0:
        종류 += 1
        existC = 1

    # print(sushi[i + 1: i + k + 1], ch, 종류)

    if sol < 종류:
        sol = 종류

    # 쿠폰 초밥에 대한 내용 되돌리기
    if existC == 1:
        종류 -= 1
        existC = 0


print(sol)
