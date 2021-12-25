def solution(d, budget):
    sum = 0
    # 작은 것부터 줘야 최대한 많이 줄 수 있으니까 오름차순 정렬하고 진행.
    d.sort()
    
    # 앞에부터 더하면서 총 금액이 예산보다 더 커지면 해당 index를 반환.
    for i in range(len(d)):
        sum += d[i]
        if sum > budget:
            return i
    else:
        return len(d)
