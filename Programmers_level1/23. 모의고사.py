import math

def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    first = first * math.ceil(len(answers) / len(first))
    second = second * math.ceil(len(answers) / len(second))
    third= third * math.ceil(len(answers) / len(third))
    
    count = [0] * 3
    
    
    for i in range(len(answers)):
        if answers[i] == first[i]:
            count[0] += 1
        if answers[i] == second[i]:
            count[1] += 1
        if answers[i] == third[i]:
            count[2] += 1


    maxCount = max(count[0], count[1], count[2])
    
    for i in range(3):
        if count[i] == maxCount:
            answer.append(i+1)
    
    
    return answer
