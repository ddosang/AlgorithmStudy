def solution(N, stages):
    # 하나 더 만들어서 0번째를 버리기로 했다.
    # 1까지 깬 사람 숫자를 헷갈리니까
    stop_count = [0] * (N+2)
    fail_ratio = [0] * (N+2)
    result = []

    
    # 해당 stage(index), 멈춘 사람 수(value) 로 하는 list 만듬.
    for stage in stages:
        stop_count[stage] += 1
        
    # 실패율 계산.
    # 해당 stage를 클리어 한 사람까지 계산해야하니까 뒤부터.
    # stage + 1 인 경우는 다 깬 사람이니까 해당 Stage 의 실패율은 계산할 필요 없어서
    # N부터 시작.
    for i in range(N, 0, -1):
        come_count = 0
        # 해당 스테이지까지 온 사람의 수를 센다.
        for j in range(N+1, i-1, -1):
            come_count += stop_count[j]
        
        # 스테이지까지 온 사람이 없으면 실패율 0으로 계산.
        if come_count == 0:
            fail_ratio[i] = 0
        else:
            fail_ratio[i] = stop_count[i] / come_count
    
        
    # 실패율에서 마지막 값은 없고,
    # 0번째 값은 계산을 편리하게 하기 위해 넣은 허수였으므로 뺀다.
    fail_ratio.pop()
    fail_ratio.pop(0)
    
    # (index, 실패율) 구조로 만들어서 실패율 기준 내림차순 정렬
    fail_ratio = list(enumerate(fail_ratio))
    fail_ratio = sorted(fail_ratio, key=lambda x:x[1], reverse=True)
    
        
    for (index, fail) in fail_ratio:
        result.append(index + 1) # 하나 빼서 0번부터 시작하고 있으므로 index에 1 더한다.
        
    return result
