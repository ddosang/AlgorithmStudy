def solution(numbers):
    answer = []
    # numbers.sort()
    
    # 자기 자신 빼고 하나씩 다 더해서 넣고, set으로 중복 제거.
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    
    answer = list(set(answer))
    answer.sort()
    
    return answer
