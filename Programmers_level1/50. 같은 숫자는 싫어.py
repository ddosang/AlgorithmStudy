def solution(arr):
    answer = [-1]
    
    for a in arr:
        if answer[-1] != a:
            answer.append(a)
    
    return answer[1:]
