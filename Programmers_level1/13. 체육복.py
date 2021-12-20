def solution(n, lost, reserve):
    answer = 0
    clothes = [1] * (n+1)
    
    for num in lost:
        clothes[num] -= 1
    for num in reserve:
        clothes[num] += 1
    
    for i in range(1, n+1):
        if clothes[i] == 2:
            if clothes[i-1] == 0:
                clothes[i] -= 1
                clothes[i-1] += 1
            elif i < n and clothes[i+1] == 0:
                clothes[i] -= 1
                clothes[i+1] += 1
    
    for i in range(1, n+1):
        if clothes[i] > 0:
            answer += 1
    
    # print(clothes)
    
    
    return answer
