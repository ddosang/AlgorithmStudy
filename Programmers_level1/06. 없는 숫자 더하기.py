def solution(numbers):
    answer = 0
    
    whole_numbers = [1,2,3,4,5,6,7,8,9,0]
    
    for num in numbers:
        whole_numbers.remove(num)
    
    
    for num in whole_numbers:
        answer += num
    
    return answer
