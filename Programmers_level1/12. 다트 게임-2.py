import re
from functools import reduce

def solution(dartResult):
    sum = 0
    pattern = re.compile("[0-9]+[SDT][*#]?")
    arr = []
    bonuses = {'S':1, 'D':2, 'T':3}
    options = {'#':-1, '*':2, '':1} # 다른 사람 풀이 보고 고친 것.
    
    splited = pattern.findall(dartResult)
    
    for s in splited:
        num = int(re.compile("[0-9]+").match(s).group())
        bonus = bonuses[re.compile("[SDT]").search(s).group()]
        option = re.compile("[*#]").search(s)
        option = option.group() if option != None else ''
        
        if option == '*' and len(arr) > 0:
            arr[-1] *= 2
        
        arr.append(num ** bonus * options[option])
        
        
    sum = reduce(lambda x, y: x+y, arr, sum) # 그냥 sum(arr) 하면 되넹...
    
    
    return sum
