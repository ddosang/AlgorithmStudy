# 240709 풀이

K = int(input())
weights = sorted(list(map(int, input().split())), reverse=True)
S = sum(weights)
res = 0
chk = [False for _ in range(S + 1)] 

def DFS(level, weight):
    if level == K:
        weight = weight if weight > 0 else -weight
        chk[weight] = True
        return
    
    # 빈 쪽 저울에 얹거나
    DFS(level + 1, weight + weights[level])
    # 물을 넣는 쪽 저울에 얹거나
    DFS(level + 1, weight - weights[level])
    # 얹지 않기.
    DFS(level + 1, weight)


DFS(0, 0)
# print(chk)
print(len(list(filter(lambda x:x==False, chk))))


# 240709 강의
K = int(input())
weights = sorted(list(map(int, input().split())), reverse=True)
S = sum(weights)
res = 0
chk = set() # set 을 사용

def DFS(level, weight):
    if level == K:
        if weight > 0: # 어차피 같은 무게가 + 인 것 하나 - 인 것 하나 생기니까 큰 것만 봐도 됨
            chk.add(weight)
        return
    
    # 빈 쪽 저울에 얹거나
    DFS(level + 1, weight + weights[level])
    # 물을 넣는 쪽 저울에 얹거나
    DFS(level + 1, weight - weights[level])
    # 얹지 않기.
    DFS(level + 1, weight)


DFS(0, 0)
# print(chk)
print(S - len(chk))
