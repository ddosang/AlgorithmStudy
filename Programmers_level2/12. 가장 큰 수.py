import re

def priority(s):
    # test case 1 ~ 6 안 된 코드
    # s += s[-1] * (4-len(s))
    for i in range(int(12 / len(s)) - 1):
        s += s

    return s
    

def solution(numbers):
    permu = ""
    
    # test case 11 번...
    if re.sub("0", '' ,''.join([str(n) for n in numbers])) == '':
        return "0"
    
    
    numbers = sorted([str(num) for num in numbers], key=lambda x:priority(x), reverse=True)
    
    return "".join(numbers)
