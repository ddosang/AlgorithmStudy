import math

def isPrime(num):
    for i in range(2, int(math.pow(num, 0.5))+1):
        if num % i == 0:
            return False
    else:

        return True

def solution(nums):
    answer = 0
    sum = 0
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                sum = nums[i] + nums[j] + nums[k]
                if isPrime(sum):
                    answer += 1

    return answer
