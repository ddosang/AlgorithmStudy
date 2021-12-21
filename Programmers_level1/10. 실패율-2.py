def solution(N, stages):
    count = [0] * (N+2)
    sum = 0
    failable = []
    result = []
    
    for stage in stages:
        count[stage] += 1

    sum = count[N+1]
    for i in range(N, 0, -1):
        sum += count[i]
        ratio = count[i] / sum if sum != 0 else 0
        failable.append([i, ratio]))
    
    
    failable = sorted(failable, key=lambda fail: fail[1])
    failable = list(map(lambda x: x[0], failable))[::-1]
    
    return failable
