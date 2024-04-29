T = int(input())
for t in range(T):
    N, L, F = map(int, input().split())
    words = list(input().split())
    ans = 0

    #  최대 공통 접미사의 길이가 F 이상이면 두 단어는 "유사 라임"

    # 단어의 길이 L
    rhyme_candidates = set()
    for i in range(N): # 처음에 여기를 L 로 해서 실패함...
        temp = words[i][-F:]
        rhyme_candidates.add(temp)
    
    rhyme_candidates = list(rhyme_candidates)

    # print(rhyme_candidates)

    for r in rhyme_candidates:
        cnt = 0
        for i in range(N):
            if r == words[i][-F:]:
                cnt += 1
        
        ans += cnt // 2
    
    print(ans)


# L 틀린지 모르고 새로 푼 것
T = int(input())
for t in range(T):
    N, L, F = map(int, input().split())
    words = sorted(list(input().split()), key=lambda x:str(x[-F:]))
    ans = 0

    
    rhyme = words[0][-F:]
    cnt = 1
    for i in range(1, N):
        # print(rhyme,  words[i][-F:])
        if rhyme != words[i][-F:]:
            rhyme = words[i][-F:]
            ans += cnt // 2
            cnt = 1
        else:
            cnt += 1

    ans += cnt // 2
            
    # anss.append(ans)
    print(ans)
