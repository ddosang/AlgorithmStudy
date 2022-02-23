from itertools import permutations
import re

def suffix(expression, order):
    
    def priority(op):
    # opStr 은 연산자가 우선순위가 낮은 것부터 나열되어 있는 스트링
        return order.index(op)


    res = []
    stack_op = []
    
    elements = re.findall("[0-9]+|[\+\-\*]", expression)
    
    for e in elements:
        if e.isdigit():
            res.append(e)
        elif e == "+" or e == "-" or e == "*":
            # 새로 들어오는 것의 우선순위가 높으면 쌓일 수 있음.
            if stack_op and priority(stack_op[-1]) < priority(e):
                stack_op.append(e)
            
            # 새로 들어오는 것의 우선순위가 낮으면 우선순위가 자기보다 낮은 것이 나올때까지 팝
            else:
                while stack_op and priority(stack_op[-1]) >= priority(e):
                    res.append(stack_op.pop())
                stack_op.append(e)

    while stack_op:
        res.append(stack_op.pop())
        
    return res

def calculateSuffix(suffixArr):
    stack_num = []
    
    for e in suffixArr:
        if e.isdigit():
            stack_num.append(int(e))
        else:
            if stack_num:
                second = stack_num.pop()
                first = stack_num.pop()
                if e == "+":
                    stack_num.append(first + second)
                elif e == "-":
                    stack_num.append(first - second)
                elif e == "*":
                    stack_num.append(first * second)
    
    return stack_num[0]
    
    
                
def solution(expression):
    answer = 0
    
    ops = re.findall("[\+\-\*]", expression)
    ops = list(set(ops))
    orders = list(permutations(ops, len(ops)))
    
    for o in orders:
        order = "".join(o)
        res = calculateSuffix(suffix(expression, order))
        res = -res if res < 0 else res
        if answer < res:
            answer = res
    
    return answer
